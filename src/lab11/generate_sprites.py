
#This code was found at the following URL, and edited to meet the requirements for this project:
#https://community.openai.com/t/howto-use-the-new-python-library-to-call-api-dall-e-and-save-and-display-images/495741

'''
DALL-E image generation example for openai>1.2.3, saves requested images as files
-- not a code utility, has no input or return

# example pydantic models returned by client.images.generate(**img_params):
## - when called with "response_format": "url":
images_response = ImagesResponse(created=1699713836, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-abcd/user-abcd/img-12345.png?st=2023-11-11T13%3A43%3A56Z&se=2023-11-11T15%3A43%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-11-10T21%3A41%3A11Z&ske=2023-11-11T21%3A41%3A11Z&sks=b&skv=2021-08-06&sig=%2BUjl3f6Vdz3u0oRSuERKPzPhFRf7qO8RjwSPGsrQ/d8%3D')])

requires:
pip install --upgrade openai
pip install pillow
'''

from io import BytesIO
import openai                  # for handling error types
import base64                  # for decoding images if recieved in the reply
from PIL import Image          # pillow, for processing image types
from openai import OpenAI

def old_package(version, minimum):  # Block old openai python libraries before today's
    version_parts = list(map(int, version.split(".")))
    minimum_parts = list(map(int, minimum.split(".")))
    return version_parts < minimum_parts

# client = OpenAI(api_key="sk-xxxxx")  # don't do this, OK?

def generate_hero():
    if old_package(openai.__version__, "1.2.3"):
        raise ValueError(f"Error: OpenAI version {openai.__version__}"
                     " is less than the minimum version 1.2.3\n\n"
                     ">>You should run 'pip install --upgrade openai')")
    client = OpenAI(api_key="sk-proj-DvPEMrANkrZqy7Pgp7J7T3BlbkFJ6RjrgU0NhpM0rJXJx2l7")  # will use environment variable "OPENAI_API_KEY"

    prompt = (
    "Subject: A sprite of an adventurous medival hero wearing a cloak and holding a sword with a transparant background "  # use the space at end
    "Style: A video game pixel art sprite." 
    )

    image_params = {
    "model": "dall-e-2", 
    "n": 1,
    "size": "256x256",
    "prompt": prompt, 
    "user": "allisonflatt", 
    }

    image_params.update({"response_format": "b64_json"})  # defaults to "url" for separate download

    # ---- START
    #Error catches
    try:
        images_response = client.images.generate(**image_params)
    except openai.APIConnectionError as e:
        print("Server connection error: {e.__cause__}")  # from httpx.
        raise
    except openai.RateLimitError as e:
        print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
        raise
    except openai.APIStatusError as e:
        print(f"OpenAI STATUS error {e.status_code}: (e.response)")
        raise
    except openai.BadRequestError as e:
        print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

    img_filename = "hero_sprite"

    image_data_list = []
    for image in images_response.data:
        image_data_list.append(image.model_dump()["b64_json"])

    image_objects = []

    if image_data_list and all(image_data_list):  # if there is b64 data
        # Convert "b64_json" data to png file
        for i, data in enumerate(image_data_list):
            image_objects.append(Image.open(BytesIO(base64.b64decode(data))))  # Append the Image object to the list
            image_objects[i].save(f"{img_filename}.png")
    else:
        print("No image data was obtained. Maybe bad code?")


def generate_bandit():
    if old_package(openai.__version__, "1.2.3"):
        raise ValueError(f"Error: OpenAI version {openai.__version__}"
                     " is less than the minimum version 1.2.3\n\n"
                     ">>You should run 'pip install --upgrade openai')")
    client = OpenAI(api_key="sk-proj-DvPEMrANkrZqy7Pgp7J7T3BlbkFJ6RjrgU0NhpM0rJXJx2l7")  # will use environment variable "OPENAI_API_KEY"

    prompt = (
    "Subject: A sprite of a bandit holding a sword with a transparant background "  # use the space at end
    "Style: A video game pixel art sprite."     # this is implicit line continuation
    )

    image_params = {
    "model": "dall-e-2",
    "n": 1,
    "size": "256x256",  
    "prompt": prompt,
    "user": "allisonflatt",
    }

    image_params.update({"response_format": "b64_json"})

    # ---- START
    # Error catching
    try:
        images_response = client.images.generate(**image_params)
    except openai.APIConnectionError as e:
        print("Server connection error: {e.__cause__}")  # from httpx.
        raise
    except openai.RateLimitError as e:
        print(f"OpenAI RATE LIMIT error {e.status_code}: (e.response)")
        raise
    except openai.APIStatusError as e:
        print(f"OpenAI STATUS error {e.status_code}: (e.response)")
        raise
    except openai.BadRequestError as e:
        print(f"OpenAI BAD REQUEST error {e.status_code}: (e.response)")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

    img_filename = "bandit_sprite"

    image_data_list = []
    for image in images_response.data:
        image_data_list.append(image.model_dump()["b64_json"])

    image_objects = []

    if image_data_list and all(image_data_list):  # if there is b64 data
        for i, data in enumerate(image_data_list):
            image_objects.append(Image.open(BytesIO(base64.b64decode(data))))  # Append the Image object to the list
            image_objects[i].save(f"{img_filename}.png")
    else:
        print("No image data was obtained. Maybe bad code?")
