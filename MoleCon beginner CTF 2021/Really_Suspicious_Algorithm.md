# Really Suspicious Algorithm - Crypto

Note: I wasn't able to submit the flag because I ran out of time, but I was able to solve it. So here we go :)

Description of the challenge: 
```
I received this secret message.
Can you decrypt it?
```

*chall.py*
```
from Crypto.Util.number import getPrime, bytes_to_long
from secret import flag

p,q = getPrime(1024), getPrime(1024)
n = p*q
e = n-p-q+4

ct = pow(bytes_to_long(flag), e, n)

print("n =", n)
print("ct =", ct)
```

*output.txt*
```
n = 24115724050507199493712762654520929936774925131059332140712511092518570415243144493303620895076999217579151352098005641220254789662082249122039429593281075763473867243116281108360849599370337166659005719677959315594442881058620733458846158693288519442417046197499609227262971291046951868872967724331630614810942937943136630611188831606642913190132779641441613453701616908620598504762030351385284494949746449796839814492726493862301122366764136396286534656293577211209070238444918749907377203907983536318913476902109610454777572292382794615391425461099601480360030664640184539023460489362835787186494390857887931724561
ct = 3339891666664090373900104605188092714288004578913068591061618601501728384543458885590673450917778514384162355873893
```


As the name of the challenge suggests, we have to break RSA. 

RSA 101: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

The problem with this instance of RSA is the exponent. If we look  it carefully, we can see that e = phi(p * q) + 3. 
phi() is Euler's totient function (https://en.wikipedia.org/wiki/Euler%27s_totient_function), and in this case phi(p * q) = phi(p) * phi(q) = (p-1)(q-1) = pq-p-q+1, since p and q are prime numbers.

So we can write e = phi(p * q) + 3 = phi(n) + 3.
Then:

flag^e % n becomes flag^(phi(n)+3) % n.  We can transform this into: (flag^(phi(n)) * flag^3) % n. 

The Euler-Fermat theorem can help us to simplify this equation. In fact, the Euler-Fermat theorem says that: x^(phi(n)) % n = 1.

So our equation becomes: flag^3 % n and this is the ct that we have in output.txt

In order to get the flag, we have to do the cube root of ct and then transform the number in bytes.


Result:
```
>>> import Crypto.Util.number
>>> import gmpy2
>>> ct = 3339891666664090373900104605188092714288004578913068591061618601501728384543458885590673450917778514384162355873893
>>> flag = gmpy2.iroot(ct,3)[0]
>>> flag = Crypto.Util.number.long_to_bytes(flag)
>>> print(flag)
b'ptm{low_exp_rsa}'
```

And here we have the flag :)
