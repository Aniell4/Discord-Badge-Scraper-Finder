from scrape import scrape
from httpx import AsyncClient
from brotli import decompress
import random, string
import os
import json
import time
import asyncio
from tasksio import TaskPool


def check_flags(flag_int):
	################
	flag_dict = {
		'Discord_Employee': 1,
		'Partnered_Server_Owner': 2,
		'HypeSquad_Events': 4,
		'Bug_Hunter_Level_1': 8,
		#'House_Bravery': 64,
		#'House_Brilliance': 128,
		#'House_Balance': 256,
		'Early_Supporter': 512,
		'Team_Pseudo_user': 1024,
		'Bug_Hunter_Level_2': 16384,
		'Verified_Bot': 65536,
		'Early_Verified_Bot_Developer': 131072,
		'Discord_Certified_moderator': 262144,
		'BOT_HTTP_INTERACIONS': 524288,
	}
	################

	flags = []
	for flag_key in flag_dict.keys():
		if ((flag_int & flag_dict[flag_key]) == flag_dict[flag_key]):
			flags.append(flag_key)

	return flags

async def main():
	members = scrape(input('[SCRAPER] Token to Scrape with: '), input('[SCRAPER] Guild ID to Scrape: '), input('[SCRAPER] Channel ID to Scrape: '))
	with open('hits.txt', 'a') as f:
		for key in members.keys():
			try:
				flags = check_flags(members[key]['public_flags'])
				if flags != []:
					f.write(key + ' - ' + ''.join(flag + ', ' for flag in flags) + '\n')
			except : pass	

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())