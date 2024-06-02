## NIfTI Files
Neuroimaging Informatics Technology Initiative is a data format for storage. Functional Magnetic Resonance Imaging (fMRI) and other medical images.
## In this, we'll be using different packages:
1. Matplotlib
2. Nibabel: It gives access to a variety of imaging formats, it provides a common interface for various formats produced by different scanners.

## Various Methods for viewing a NIfTI file
### 1. Load NIfTI file
```
brain_vol = nib.load("") #Enter the path to NIfTI file here
type(brain_vol)
```
### 2. View Metadata
```
print(brain_vol.header)
```
### Output
```
<class 'nibabel.nifti1.Nifti1Header'> object, endian='<'
sizeof_hdr      : 348
data_type       : b''
db_name         : b''
extents         : 0
session_error   : 0
regular         : b'r'
dim_info        : 54
dim             : [  3 192 256 256   1   1   1   1]
intent_p1       : 0.0
intent_p2       : 0.0
intent_p3       : 0.0
intent_code     : none
datatype        : int16
bitpix          : 16
slice_start     : 0
pixdim          : [1.  1.  1.  1.  2.3 0.  0.  0. ]
vox_offset      : 0.0
scl_slope       : nan
scl_inter       : nan
slice_end       : 0
slice_code      : unknown
xyzt_units      : 10
cal_max         : 0.0
cal_min         : 0.0
slice_duration  : 0.0
toffset         : 0.0
glmax           : 0
glmin           : 0
descrip         : b'TE=2.7;Time=150734.828;phase=1'
aux_file        : b''
qform_code      : scanner
sform_code      : scanner
quatern_b       : 0.00042526424
quatern_c       : -0.027039066
quatern_d       : 0.01571919
qoffset_x       : -81.5222
qoffset_y       : -130.72974
qoffset_z       : -144.47054
srow_x          : [ 9.9804670e-01 -3.1445995e-02 -5.4038301e-02 -8.1522202e+01]
srow_y          : [ 3.1400096e-02  9.9950546e-01 -1.7001767e-03 -1.3072974e+02]
srow_z          : [ 5.4065209e-02  4.7863640e-08  9.9853742e-01 -1.4447054e+02]
intent_name     : b''
magic           : b'n+1'
```
### 3. Access data in the NIfTI object
```
brain_vol_data = brain_vol.get_fdata()
type(brain_vol_data)
```
### Output
```
numpy.ndarray
```
### Dimensions of the image
```
brain_vol_data.shape
```
### Output
```
(192, 256, 256)
```
### 4. Visualize a Slice
```
plt.imshow(brain_vol_data[96], cmap='bone')
plt.axis('off')
plt.show()
```




