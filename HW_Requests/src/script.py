from lib import GetInformationBank, PostGoogleTranslate

Bank = GetInformationBank()
Bank.write_response_from_server()

Translation = PostGoogleTranslate(sentence='I am from Kiev')
print(Translation.get_translation())