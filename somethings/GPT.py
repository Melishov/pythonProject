import g4f

from g4f.Provider import (
    Bard,
    Bing,
    HuggingChat,
    OpenAssistant,
    OpenaiChat,
)

# Usage:
response = g4f.ChatCompletion.create(
    model=g4f.models.default,
    messages=[{"role": "user", "content": "Hello"}],
    provider=Bard,
    #cookies=g4f.get_cookies(".google.com"),
    cookies={"cookie_name": "value", "cookie_name2": "value2"},
    auth=True
)