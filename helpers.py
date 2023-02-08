import uuid as uuid
from werkzeug.utils import secure_filename
from env_keys.env_secrets import BLOB_NAME, BLOB_KEY, BLOB_STRING, BLOB_CONTAINER_NAME
from azure.storage.blob import BlobServiceClient
UPLOAD_FOLDER = 'static/profile_imgs'
blob_service_client = BlobServiceClient.from_connection_string(
    conn_str=BLOB_STRING)
container_client = blob_service_client.get_container_client(
    container=BLOB_CONTAINER_NAME)


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
        blob_client = container_client.get_blob_client(db_img_name)
        blob_client.upload_blob(profile_img)
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
        blob_client2 = container_client.get_blob_client(db_img_name)
        blob_client2.upload_blob(profile_img)
        # delete old image from azuer
        if user.image_filename:
            try:
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
        container_client.delete_blob(image)
    except Exception as e:
        print(e)
