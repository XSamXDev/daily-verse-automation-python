from email_send import send_email
from verse_scraping import scrape_daily_verse


def automation():
    data = scrape_daily_verse()

    message = f""" <!DOCTYPE html> <html> <head> <meta charset="UTF-8"> </head> <body style=" margin: 0; padding: 30px 15px; background-color: #f4f4f4; font-family: Arial, sans-serif; "> <div style=" max-width: 600px; margin: auto; background: white; border-radius: 12px; padding: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); "> <div style=" background-color: #f8f8f8; border-radius: 10px; padding: 20px; margin-bottom: 20px; "> <p style=" font-size: 20px; line-height: 1.8; color: #222; margin: 0; "> {data["english"]} </p> </div> <div style=" background-color: #fafafa; border-radius: 10px; padding: 20px; margin-bottom: 25px; direction: rtl; "> <p style=" font-size: 25px; line-height: 2; color: #111; text-align: right; margin: 0; "> {data["arabic"]} </p> </div> <div style=" text-align: center; padding-top: 15px; border-top: 1px solid #ddd; "> <p style=" font-size: 16px; font-weight: bold; color: #444; "> Surah {data["surah"]} [{data["verse"]}] </p> </div> </div> </body> </html> """

    send_email(message)


if __name__ == "__main__":
    automation()
