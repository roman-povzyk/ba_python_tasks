# Write a decorator that takes a list of stop
# words and replaces them with *inside the decorated function
def stop_words(words: list):
    def wrapper(func):
        def string(*args, **kwargs):
            """Переписуємо поведінку нашої функції"""
            our_str = str(func(*args, **kwargs))
            for word in words:
                if word.lower() in our_str.lower():
                    our_str = our_str.replace(word, '*')
            return our_str
        return string
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


print(create_slogan('Roman'))
