#--
#-- ************************************************************************************************************:
#-- ******************************************* EXIF DATA FROM PHOTO *******************************************:
#-- ************************************************************************************************************:
#-- Author:   JBALLARD (JEB)                                                                                    :
#-- Date:     2023.2.18                                                                                         :
#-- Script:   GET-EXIF.PHOTO.DATA.py                                                                            :
#-- Purpose:  A python script that retrieves the EXIF data from a photo.                                        :
#-- Class:    python -m pip install pillow                                                                      :
#-- Class:    python -m pip install ExifRead                                                                    :
#-- Version:  1.0                                                                                               :
#-- ************************************************************************************************************:
#-- ************************************************************************************************************:
#--
#-- ********************************************************:
#-- DEFINE PARAMS, CONSTANTS, CONFIG PATHS, IMPORT CLASSES  :
#-- ********************************************************:
import PIL.Image
import PIL.ExifTags
import exifread
#--
def get_exif_data_method1(image_path):
    img = PIL.Image.open(image_path)
    exif_data = {
        PIL.ExifTags.TAGS[i]: j
        for i, j in img._getexif().items()
        if i in PIL.ExifTags.TAGS
    }
    return exif_data
#--
if __name__ == "__main__":
    image_path = "Img.jpg"
    exif_data = get_exif_data_method1(image_path)
    print(exif_data)
#--
def get_exif_data_method2(image_path):
    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file)
    return tags
#--
if __name__ == "__main__":
    image_path = "Img.jpg"
    exif_data = get_exif_data_method2(image_path)
    print(exif_data)
#--
#-- ********************************************************:
#-- END OF PYTHON SCRIPT                                    :
#-- ********************************************************: