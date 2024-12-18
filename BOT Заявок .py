from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Используйте свои данные для токена бота и файла учетных данных Google
TOKEN = ''
CREDENTIALS_FILE = ''

# Настройка Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)

# Откройте таблицу по URL
sheet = client.open_by_url('').sheet1

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Пожалуйста, отправьте мне свое имя и номер в формате: Имя, Номер')

def save_to_sheet(update: Update, context: CallbackContext) -> None:
    text = update.message.text.split(',')
    if len(text) == 2:
        name, number = text
        sheet.append_row([name.strip(), number.strip()])
        update.message.reply_text('Ваша информация была успешно сохранена!')
    else:
        update.message.reply_text('Пожалуйста, следуйте формату: Имя, Номер')

def main() -> None:
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, save_to_sheet))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
