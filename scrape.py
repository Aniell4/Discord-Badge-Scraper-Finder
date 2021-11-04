import discum

def scrape(token, guild_id, channel_id):
	bot = discum.Client(token=token, log=None)

	def close_after_fetching(resp, guild_id):
		if bot.gateway.finishedMemberFetching(guild_id):
			lenmembersfetched = len(bot.gateway.session.guild(guild_id).members) #this line is optional
			print('[SCRAPER] '+str(lenmembersfetched)+' Members Fetched') #this line is optional
			bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
			bot.gateway.close()

	def get_members(guild_id, channel_id):
		bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0.05) #get all user attributes, wait 0.05 second between requests
		bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
		bot.gateway.run()
		bot.gateway.resetSession() #saves 10 seconds when gateway is run again
		return bot.gateway.session.guild(guild_id).members

	return get_members(guild_id, channel_id) #yes, the channel_id input is required

if __name__ == '__main__':
	members = scrape('ODg0MDM5ODMyMTk0NjQ2MDE3.YTStKg.2DAPuKHDzjV9-lIw5K51Qh_Kz_M', '832843345503846410', '832858154332979250')
	with open('data/ids.txt', 'w') as t:
		data = ''
		for member in members:
			data += member + '\n'
		t.write(data)