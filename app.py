from flask import Flask, render_template, request

app = Flask(__name__)

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        n = int(request.form['n'])
        prime_numbers = sieve_of_eratosthenes(n)
    else:
        prime_numbers = []

    return render_template('index.html', primes=prime_numbers)

if __name__ == '__main__':
    app.run()
