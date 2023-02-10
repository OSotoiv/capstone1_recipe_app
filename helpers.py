import uuid as uuid
import os
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobClient, ContainerClient
# from env_keys.env_secrets import BLOB_CONTAINER_NAME, BLOB_STRING, BLOB_CON_SAS_TOKEN
UPLOAD_FOLDER = 'static/profile_imgs'


def save_user_images(form):
    """this helper saves images to database then returns the form to create/updata a User"""
    profile_img = form.image_url.data

    # if image_url (users profile pic) not null and file type is allowed
    if profile_img:
        # make sure file name is secure
        profile_img_filename = secure_filename(profile_img.filename)
        # unique naming file with uuid
        db_img_name = str(uuid.uuid1()) + '_' + profile_img_filename
        # change filename on acutual file and save
        profile_img.filename = db_img_name
        try:
            blob_client = BlobClient.from_connection_string(
                conn_str=os.environ.get('BLOB_STRING', "BLOB_STRING"),
                container_name=os.environ.get(
                    'BLOB_CONTAINER_NAME', "BLOB_CONTAINER_NAME"),
                blob_name=db_img_name,
                credential=os.environ.get('BLOB_CON_SAS_TOKEN', "BLOB_CON_SAS_TOKEN"))
            blob_client.upload_blob(profile_img)
        except Exception as e:
            print(e)
            form.image_url.data.url = ""
            form.image_url.data.filename = ""
            form.image_url.data = ""
            return form
        # profile_img.save(os.path.join(UPLOAD_FOLDER, db_img_name))
        form.image_url.data.url = blob_client.url
        form.image_url.data.filename = db_img_name
    return form


def update_user_images(form, user):
    # check if the user is updating the user image
    profile_img = form.image_url.data
    if profile_img and profile_img != user.image_url:
        # make sure file name is secure
        profile_img_filename = secure_filename(profile_img.filename)
        # unique naming file with uuid
        db_img_name = str(uuid.uuid1()) + '_' + profile_img_filename
        # change filename on acutual file and save
        profile_img.filename = db_img_name
        blob_client2 = BlobClient.from_connection_string(
            conn_str=os.environ.get('BLOB_STRING', "BLOB_STRING"),
            container_name=os.environ.get(
                'BLOB_CONTAINER_NAME', "BLOB_CONTAINER_NAME"),
            blob_name=db_img_name,
            credential=os.environ.get("BLOB_CON_SAS_TOKEN", "BLOB_CON_SAS_TOKEN"))
        blob_client2.upload_blob(profile_img)
        # delete old image from azuer
        if user.image_filename:
            try:
                container_client = ContainerClient.from_connection_string(
                    conn_str=os.environ.get('BLOB_STRING', "BLOB_STRING"),
                    container_name=os.environ.get(
                        'BLOB_CONTAINER_NAME', "BLOB_CONTAINER_NAME"),
                    credential=os.environ.get("BLOB_CON_SAS_TOKEN", "BLOB_CON_SAS_TOKEN"))
                container_client.delete_blob(user.image_filename)
            except Exception as e:
                print(e)

        # profile_img.save(os.path.join(UPLOAD_FOLDER, db_img_name))
        form.image_url.filename = profile_img.filename
        form.image_url.url = blob_client2.url
    else:
        form.image_url.filename = user.image_filename
        form.image_url.url = user.image_url
    return form


def remove_img_from_azuer(image):
    try:
        container_client = ContainerClient.from_connection_string(
            conn_str=os.environ.get('BLOB_STRING', "BLOB_STRING"),
            container_name=os.environ.get(
                'BLOB_CONTAINER_NAME', "BLOB_CONTAINER_NAME"),
            credential=os.environ.get('BLOB_CON_SAS_TOKEN', "BLOB_CON_SAS_TOKEN"))

        container_client.delete_blob(image)
    except Exception as e:
        print(e)
