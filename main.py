from html import escape

from dua import fetch_dua
from email_send import send_email
from sunnah import fetch_hadith
from verse_scraping import scrape_daily_verse


def automation():
    verse = scrape_daily_verse()
    hadith = fetch_hadith()
    dua = fetch_dua()

    # Escape scraped content before inserting it into HTML
    verse_arabic = escape(str(verse["arabic"]))
    verse_english = escape(str(verse["english"]))
    verse_surah = escape(str(verse["surah"]))
    verse_number = escape(str(verse["verse"]))

    hadith_arabic = escape(str(hadith["arabic"]))
    hadith_english = escape(str(hadith["english"]))
    hadith_collection = escape(str(hadith["collection_name"]))
    hadith_number = escape(str(hadith["hadithnumber"]))

    dua_arabic = escape(str(dua["arabic"]))
    dua_transliteration = escape(str(dua["arabic_english"]))
    dua_english = escape(str(dua["english"]))
    dua_source = escape(str(dua["source"]))

    message = f"""
<!DOCTYPE html>
<html>

<body style="
    margin:0;
    padding:0;
    background-color:#f3f5f4;
    font-family:Arial, Helvetica, sans-serif;
    color:#25332e;
">

    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#f3f5f4; padding:30px 12px;">
        <tr>
            <td align="center">

                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="
           max-width:640px;
           background-color:#ffffff;
           border-radius:16px;
           overflow:hidden;
       ">

                    <!-- HEADER -->
                    <tr>
                        <td style="
    background-color:#173f35;
    padding:32px 25px;
    text-align:center;
">



                            <div style="
        font-size:29px;
        line-height:1.3;
        font-weight:bold;
        color:#ffffff;
        margin-top:10px;
    ">
                                Daily Islamic Reminder
                            </div>


                        </td>
                    </tr>


                    <!-- ==================== VERSE ==================== -->

                    <tr>
                        <td style="padding:30px 25px 15px 25px;">

                            <div style="
        font-size:12px;
        letter-spacing:2px;
        font-weight:bold;
        color:#6d9f8d;
        text-transform:uppercase;
        margin-bottom:8px;
    ">
                                Verse of the Day
                            </div>

                            <!-- Arabic -->
                            <div style="
        background-color:#f7faf8;
        border-radius:12px;
        padding:25px 20px;
        direction:rtl;
        margin-bottom:20px;
    ">

                                <p style="
            font-size:27px;
            line-height:2.1;
            color:#17221e;
            text-align:right;
            margin:0;
        ">
                                    {verse_arabic}
                                </p>

                            </div>

                            <!-- Translation -->
                            <div style="
        border-left:3px solid #6d9f8d;
        padding-left:16px;
        margin-bottom:20px;
    ">

                                <p style="
            font-size:17px;
            line-height:1.85;
            color:#35443e;
            margin:0;
        ">
                                    {verse_english}
                                </p>

                            </div>

                            <!-- Reference -->
                            <div style="
        text-align:center;
        padding:15px;
        background-color:#fafbfa;
        border-radius:10px;
    ">

                                <span style="
            font-size:14px;
            font-weight:bold;
            color:#52615b;
        ">
                                    Surah {verse_surah}
                                </span>

                                <span style="
            font-size:13px;
            color:#89938f;
        ">
                                    &nbsp;•&nbsp; Ayah {verse_number}
                                </span>

                            </div>

                        </td>
                    </tr>


                    <!-- DIVIDER -->
                    <tr>
                        <td style="padding:15px 25px;">
                            <div style="height:1px;background-color:#e5e9e7;"></div>
                        </td>
                    </tr>


                    <!-- ==================== HADITH ==================== -->

                    <tr>
                        <td style="padding:10px 25px 25px 25px;">

                            <div style="
        font-size:12px;
        letter-spacing:2px;
        font-weight:bold;
        color:#6d9f8d;
        text-transform:uppercase;
        margin-bottom:8px;
    ">
                                Hadith of the Day
                            </div>


                            <!-- Arabic -->
                            <div style="
        background-color:#f7faf8;
        border-radius:12px;
        padding:25px 20px;
        direction:rtl;
        margin-bottom:20px;
    ">

                                <p style="
            font-size:25px;
            line-height:2;
            color:#17221e;
            text-align:right;
            margin:0;
        ">
                                    {hadith_arabic}
                                </p>

                            </div>

                            <!-- English -->
                            <div style="
        border-left:3px solid #6d9f8d;
        padding-left:16px;
        margin-bottom:20px;
    ">

                                <p style="
            font-size:17px;
            line-height:1.85;
            color:#35443e;
            margin:0;
        ">
                                    {hadith_english}
                                </p>

                            </div>

                            <!-- Reference -->
                            <div style="
        text-align:center;
        padding:15px;
        background-color:#fafbfa;
        border-radius:10px;
    ">

                                <div style="
            font-size:14px;
            font-weight:bold;
            color:#52615b;
        ">
                                    {hadith_collection}
                                </div>

                                <div style="
            font-size:13px;
            color:#89938f;
            margin-top:5px;
        ">
                                    Hadith #{hadith_number}
                                </div>

                            </div>

                        </td>
                    </tr>


                    <!-- DIVIDER -->
                    <tr>
                        <td style="padding:0 25px 15px 25px;">
                            <div style="height:1px;background-color:#e5e9e7;"></div>
                        </td>
                    </tr>


                    <!-- ==================== DUA ==================== -->

                    <tr>
                        <td style="padding:10px 25px 30px 25px;">

                            <div style="
        font-size:12px;
        letter-spacing:2px;
        font-weight:bold;
        color:#6d9f8d;
        text-transform:uppercase;
        margin-bottom:8px;
    ">
                                Dua of the Day
                            </div>

                            <!-- Arabic -->
                            <div style="
        background-color:#f7faf8;
        border-radius:12px;
        padding:25px 20px;
        direction:rtl;
        margin-bottom:18px;
    ">

                                <p style="
            font-size:27px;
            line-height:2.1;
            color:#17221e;
            text-align:right;
            margin:0;
        ">
                                    {dua_arabic}
                                </p>

                            </div>

                            <!-- Transliteration -->
                            <div style="
        background-color:#fafbfa;
        border-radius:10px;
        padding:16px 18px;
        margin-bottom:18px;
    ">

                                <p style="
            font-size:15px;
            line-height:1.8;
            color:#68756f;
            font-style:italic;
            margin:0;
        ">
                                    {dua_transliteration}
                                </p>

                            </div>

                            <!-- Meaning -->
                            <div style="
        border-left:3px solid #6d9f8d;
        padding-left:16px;
        margin-bottom:20px;
    ">

                                <p style="
            font-size:17px;
            line-height:1.85;
            color:#35443e;
            margin:0;
        ">
                                    {dua_english}
                                </p>

                            </div>

                            <!-- Source -->
                            <div style="
        text-align:center;
        padding-top:15px;
        border-top:1px solid #e5e9e7;
    ">

                                <span style="
            font-size:13px;
            color:#89938f;
        ">
                                    Source: {dua_source}
                                </span>

                            </div>

                        </td>
                    </tr>


                    <!-- FOOTER -->
                    <tr>
                        <td style="
    background-color:#173f35;
    padding:22px 25px;
    text-align:center;
">

                            <div style="
        font-size:14px;
        color:#dce9e4;
        line-height:1.7;
    ">
                                May these reminders bring benefit, reflection, and guidance.
                            </div>

                            <div style="
        font-size:12px;
        color:#9fbbb1;
        margin-top:8px;
    ">
                                Daily Islamic Reminder
                            </div>

                        </td>
                    </tr>

                </table>

            </td>
        </tr>
    </table>

</body>

</html>"""
    send_email(message)


if __name__ == "__main__":
    automation()
