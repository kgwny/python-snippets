from itertools import accumulate

def str_clamp_bytes(value: str, max_bytes: int) -> str:
    byte_count = (len(s.encode("utf-8")) for s in value)
    try:
        end_slice = next(i for i, v in enumerate(accumulate(byte_count)) if v > max_bytes)
    except StopIteration:
        return value
    return value[:end_slice]

print(str_clamp_bytes("hogeikatakopiyo", 8))
print(str_clamp_bytes("akasatanahamayarawa", 12))
