import os
import dotenv

dotenv.load_dotenv()


token = os.getenv('BOT_TOKEN')
admins_ids = os.getenv('ADMIN_IDS')
