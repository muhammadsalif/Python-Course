{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python version\n",
      "3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]\n",
      "Version info.\n",
      "sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(\"Python version\")\n",
    "print (sys.version)\n",
    "print(\"Version info.\")\n",
    "print (sys.version_info)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Today's date: 2019-11-02\n"
     ]
    }
   ],
   "source": [
    "from datetime import date\n",
    "today = date.today()\n",
    "print(\"Today's date:\", today)"
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
      "Input the radius of the circle : 2.14\n",
      "The area of the circle with radius 2.14 is: 14.387237716379817\n"
     ]
    }
   ],
   "source": [
    "from math import pi\n",
    "r = float(input (\"Input the radius of the circle : \"))\n",
    "print (\"The area of the circle with radius \" + str(r) + \" is: \" + str(pi * r**2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input your First Name : Sami\n",
      "Input your Last Name : Tariq\n",
      "Hello  Tariq Sami\n"
     ]
    }
   ],
   "source": [
    "fname = input(\"Input your First Name : \")\n",
    "lname = input(\"Input your Last Name : \")\n",
    "print (\"Hello  \" + lname + \" \" + fname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number: 1\n",
      "Enter second number: 2\n",
      "The sum of 1 and 2 is 3.0\n"
     ]
    }
   ],
   "source": [
    "num1 = input('Enter first number: ')\n",
    "num2 = input('Enter second number: ')\n",
    "# Add two numbers\n",
    "sum = float(num1) + float(num2)\n",
    "# Display the sum\n",
    "print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))"
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
      "\n",
      "Twinkle, twinkle, little star,\n",
      "How I wonder what you are!\n",
      "Up above the world so high,\n",
      "Like a diamond in the sky.\n",
      "Twinkle, twinkle, little star,\n",
      "How I wonder what you are!\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print('''\n",
    "Twinkle, twinkle, little star,\n",
    "How I wonder what you are!\n",
    "Up above the world so high,\n",
    "Like a diamond in the sky.\n",
    "Twinkle, twinkle, little star,\n",
    "How I wonder what you are!\n",
    "''')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
