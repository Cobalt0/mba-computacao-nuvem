# The GDAL C library, OGR exception, and the Field object
from django.contrib.gis.gdal.base import GDALBase
from django.contrib.gis.gdal.error import OGRException, OGRIndexError
from django.contrib.gis.gdal.field import Field
from django.contrib.gis.gdal.geometries import OGRGeometry, OGRGeomType

# ctypes function prototypes
from django.contrib.gis.gdal.prototypes import ds as capi, geom as geom_api

from django.utils.encoding import force_bytes, force_text
from django.utils import six
from django.utils.six.moves import xrange


# For more information, see the OGR C API source code:
#  http://www.gdal.org/ogr/ogr__api_8h.html
#
# The OGR_F_* routines are relevant here.
class Feature(GDALBase):
    """
    This class that wraps an OGR Feature, needs to be instantiated
    from a Layer object.
    """

    #### Python 'magic' routines ####
    def __init__(self, feat, layer):
        """
        Initializes Feature from a pointer and its Layer object.
        """
        if not feat:
            raise OGRException('Cannot create OGR Feature, invalid pointer given.')
        self.ptr = feat
        self._layer = layer

    def __del__(self):
        "Releases a reference to this object."
        if self._ptr:
            capi.destroy_feature(self._ptr)

    def __getitem__(self, index):
        """
        Gets the Field object at the specified index, which may be either
        an integer or the Field's string label.  Note that the Field object
        is not the field's _value_ -- use the `get` method instead to
        retrieve the value (e.g. an integer) instead of a Field instance.
        """
        if isinstance(index, six.string_types):
            i = self.index(index)
        else:
            if index < 0 or index > self.num_fields:
                raise OGRIndexError('index out of range')
            i = index
        return Field(self, i)

    def __iter__(self):
        "Iterates over each field in the Feature."
        for i in xrange(self.num_fields):
            yield self[i]

    def __len__(self):
        "Returns the count of fields in this feature."
        return self.num_fields

    def __str__(self):
        "The string name of the feature."
        return 'Feature FID %d in Layer<%s>' % (self.fid, self.layer_name)

    def __eq__(self, other):
        "Does equivalence testing on the features."
        return bool(capi.feature_equal(self.ptr, other._ptr))

    #### Feature Properties ####
    @property
    def encoding(self):
        return self._layer._ds.encoding

    @property
    def fid(self):
        "Returns the feature identifier."
        return capi.get_fid(self.ptr)

    @property
    def layer_name(self):
        "Returns the name of the layer for the feature."
        name = capi.get_feat_name(self._layer._ldefn)
        return force_text(name, self.encoding, strings_only=True)

    @property
    def num_fields(self):
        "Returns the number of fields in the Feature."
        return capi.get_feat_field_count(self.ptr)

    @property
    def fields(self):
        "Returns a list of fields in the Feature."
        return [capi.get_field_name(capi.get_field_defn(self._layer._ldefn, i))
                for i in xrange(self.num_fields)]

    @property
    def geom(self):
        "Returns the OGR Geometry for this Feature."
        # Retrieving the geometry pointer for the feature.
        geom_ptr = capi.get_feat_geom_ref(self.ptr)
        return OGRGeometry(geom_api.clone_geom(geom_ptr))

    @property
    def geom_type(self):
        "Returns the OGR Geometry Type for this Feture."
        return OGRGeomType(capi.get_fd_geom_type(self._layer._ldefn))

    #### Feature Methods ####
    def get(self, field):
        """
        Returns the value of the field, instead of an instance of the Field
        object.  May take a string of the field name or a Field object as
        parameters.
        """
        field_name = getattr(field, 'name', field)
        return self[field_name].value

    def index(self, field_name):
        "Returns the index of the given field name."
        i = capi.get_field_index(self.ptr, force_bytes(field_name))
        if i < 0:
            raise OGRIndexError('invalid OFT field name given: "%s"' % field_name)
        return i
