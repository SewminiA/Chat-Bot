import re
import response as res

def words_probability(utilizer_words, recognised_words, single_reply=False, required_words=[]):
    words_guarantee = 0

    for word in utilizer_words:
        if word in recognised_words:
            words_guarantee += 1

    for word in required_words:
        if word not in utilizer_words:
            return 0

    words_percentage = float(words_guarantee) / float(len(recognised_words))

    if single_reply:
        return int(words_percentage * 100)
    else:
        return 0

def check_all(message):
    high_probability_list = {}

    def reply(bot_reply, words_list, single_reply, required_words=[]):
        nonlocal high_probability_list
        high_probability_list[bot_reply] = words_probability(message, words_list, single_reply, required_words)

    reply('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_reply=True)
    reply("I'm doing fine, and you?", ['how', 'are', 'you', 'doing'], single_reply=True, required_words=['how'])
    reply('Thank you', ['I', 'Love', 'code', 'palace'], single_reply=True, required_words=['code', 'palace'])
    reply(res.R_EATING, ['what', 'you', 'eat'], single_reply=True, required_words=['you', 'eat'])

    best_match = max(high_probability_list, key=high_probability_list.get)

    return res.unknown() if high_probability_list[best_match] < 1 else best_match

def get_reply(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all(split_message)

# Testing the reply system
while True:
    user_input = input('You: ')
    print('Bot:', get_reply(user_input))
