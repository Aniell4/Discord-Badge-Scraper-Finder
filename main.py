from scrape import scrape
import asyncio


def check_flags(flag_int):
    flag_dict = {
        "Discord_Employee": 1,
        "Partnered_Server_Owner": 2,
        "HypeSquad_Events": 4,
        "Bug_Hunter_Level_1": 8,
        "Early_Supporter": 512,
        "Team_Pseudo_user": 1024,
        "Bug_Hunter_Level_2": 16384,
        "Verified_Bot": 65536,
        "Early_Verified_Bot_Developer": 131072,
        "Discord_Certified_moderator": 262144,
        "BOT_HTTP_INTERACIONS": 524288,
    }

    # fixed it for u lil bro
    flags = []
    for flag_key, flag_value in flag_dict.items():
        if flag_int & flag_value:
            flags.append(flag_key)

    return flags


async def main():
    members = scrape(
        input("[SCRAPER] Token to Scrape with: "),
        input("[SCRAPER] Guild ID to Scrape: "),
        input("[SCRAPER] Channel ID to Scrape: "),
    )
    with open("hits.txt", "a") as f:
        for key in members.keys():
            try:
                flags = check_flags(members[key]["public_flags"])
                if flags != []:
                    f.write(key + " - " + "".join(flag + ", " for flag in flags) + "\n")
            except:
                pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
