# using lookup tables
# generating english words from numbers, complying british numbers
# https://english.stackexchange.com/questions/111765/how-to-write-out-numbers-in-compliance-with-british-usage

def compute():
    return sum(len(to_english(n)) for n in range(1, 1001))

ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
TWENTIES = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def to_english(n):
    if n >= 0 and n <= 10:
        sen = ONES[n]
    elif n > 10 and n < 20:
        sen = TWENTIES[n%10]
    elif n >= 20 and n < 100:
        sen = TENS[n//10] + ONES[n%10]
    elif n >= 100 and n < 1000:
        sen = ONES[n//100] + 'hundred'
        if n%100 != 0: sen += 'and'
        sen += to_english(n%100)
    elif n >= 1000 and n < 1000000:
        sen = to_english(n//1000) + 'thousand'
        if n%1000 < 100 and n%1000 > 0: sen += 'and'
        sen += to_english(n%1000)
    return sen

if __name__ == "__main__":
    print(compute())