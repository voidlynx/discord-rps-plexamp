from services.config import config
from typing import Optional
from utils.logging import logger
import requests

# i won't bother renaming this one. even tho its not imgur now >:3

def uploadImage(url: str) -> Optional[str]:
	try:
		data = requests.post(
			"https://" + config["display"]["posters"]["cuDomain"] + "/upload",
			data = { "secret": config['display']['posters']['cuSecret'] },
			files = { "image": requests.get(url).content }
		).json()
		if "message" not in data:
			raise Exception(data["error"])
		return "https://" + config["display"]["posters"]["cuDomain"] + "/cover.jpg"
	except:
		logger.exception("An unexpected error occured while uploading an image")
