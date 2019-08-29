import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23

}

params_str = json.dumps(params)
print("after json serialization")
print('type of params_str = {}, params_str = {}'.format(type(params_str), params))

print('#' * 8 + '输出' + '#' * 8)

original_params = json.loads(params_str)

print('after the json deserialization')
print('type of  original_params = {} original_params = {}'.format(
    type(original_params), original_params))
