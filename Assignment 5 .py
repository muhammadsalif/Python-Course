{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the factorial of number is 120\n"
     ]
    }
   ],
   "source": [
    "#Q.1 factorial of a number\n",
    "def func(n):\n",
    "    b = 1\n",
    "    vb = n\n",
    "    for a in range(n , 0 , -1): \n",
    "        b = b * a\n",
    "    print('the factorial of number is ' + str(b))\n",
    "    return\n",
    "func(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of  upper capital letter 2\n",
      "number of lower case letter 4\n"
     ]
    }
   ],
   "source": [
    "#q.2 upper case lower case letter\n",
    "def func(st):\n",
    "    name = st\n",
    "    l = 0\n",
    "    c = 0\n",
    "    for x in name:\n",
    "        vb1 = x.islower()\n",
    "        if vb1 == True:\n",
    "            l = l + 1 \n",
    "        elif vb1 == False:\n",
    "            c = c + 1\n",
    "    print('number of  upper capital letter ' + str(c))\n",
    "    print('number of lower case letter ' + str(l))\n",
    "    return\n",
    "\n",
    "func('pyTHon')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "6\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "#Q3 even number\n",
    "ls = [3,2,6,7,8,9]\n",
    "def even(ls):\n",
    "    list1 = ls\n",
    "    for a in list1:\n",
    "        if a % 2 == 0:\n",
    "            print(a)\n",
    "            \n",
    "even(ls)            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "madam\n",
      "given variable is palindrome\n"
     ]
    }
   ],
   "source": [
    "#Q4 palindrome\n",
    "def my_func(st):\n",
    "        \n",
    "    ls = []\n",
    "    rev = st[::-1]\n",
    "    print(rev)\n",
    "    for x in rev:\n",
    "        ls.append(x)\n",
    "    \n",
    "    a = 0    \n",
    "    i = 0\n",
    "    for x in st:\n",
    "        vb1 = ls.pop(i)\n",
    "        vb1 = str (vb1)\n",
    "        x = str(x) \n",
    "        if vb1 != x:\n",
    "            print('given variable is not palindrome')\n",
    "            a = 1\n",
    "            break\n",
    "        \n",
    "    if a != 1:\n",
    "        print('given variable is palindrome')\n",
    "    \n",
    "    return  \n",
    "my_func('madam')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is prime \n"
     ]
    }
   ],
   "source": [
    "#Q5 prime number\n",
    "def func(a):\n",
    "    vb = 0\n",
    "    no = a\n",
    "    for b in range(2,no):\n",
    "        if no % b == 0:\n",
    "            print('number is not prime ')\n",
    "            vb = 1\n",
    "            break\n",
    "    if vb == 0:\n",
    "        print('number is prime ')\n",
    "    return\n",
    "func(11)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user purchased following item  : \n",
      "bat\n",
      "ball\n",
      "football\n"
     ]
    }
   ],
   "source": [
    "# Q.6\n",
    "def func(a,b,c):\n",
    "    print('user purchased following item  : '  \n",
    "         +'\\n'+ a +'\\n'+  b +'\\n'+ c)\n",
    "    return \n",
    "func('bat' , 'ball' ,'football')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
