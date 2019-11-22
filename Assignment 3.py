{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first value 5\n",
      "Enter second value 3\n",
      "Select Any Operator **\n",
      "125 answer\n"
     ]
    }
   ],
   "source": [
    "m = int(input(\"Enter first value \"))\n",
    "a = int(input(\"Enter second value \"))\n",
    "operator = (input (\"Select Any Operator \"))\n",
    "\n",
    "if operator == '+':\n",
    "    z = m + a\n",
    "    print (z,'answer')\n",
    "elif operator == '-':\n",
    "    z = m - a\n",
    "    print (z,'answer')\n",
    "elif operator == '*':\n",
    "    z = m * a\n",
    "    print (z,'answer')\n",
    "elif operator == '/':\n",
    "    z = m / a\n",
    "    print (z,'answer')\n",
    "if operator == '**':\n",
    "    z = m ** a\n",
    "    print (z,'answer')\n",
    "else:\n",
    "    print(\"You Put inappropriate operator\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "55\n",
      "900\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"Apple\", \"Mango\", \"Banana\", \"Karachi\", 55, 900, 5]\n",
    "for a_numeric_number in list1:\n",
    "    if type(a_numeric_number) == int:\n",
    "        print(a_numeric_number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first name': 'Bill', 'last name': 'Gates', 'language': 'English', 'country': 'USA'}\n"
     ]
    }
   ],
   "source": [
    "customer = {\n",
    "    \"first name\": \"Bill\",\n",
    "    \"last name\": \"Gates\",\n",
    "    \"language\": \"English\"\n",
    "}\n",
    "customer[\"country\"] = 'USA'\n",
    "print(customer)"
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
      "Sum of all numeric items in a dict  11\n"
     ]
    }
   ],
   "source": [
    "customer = {\n",
    "    'a': 4,\n",
    "    'b': 1,\n",
    "    'c': 6,\n",
    "    'd': 'apple'\n",
    "}\n",
    "sum = 0\n",
    "for i in customer.values():\n",
    "    if type(i) == int:\n",
    "        sum += i\n",
    "print(\"Sum of all numeric items in a dict \",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "duplicate value is Apple\n",
      "duplicate value is 55\n"
     ]
    }
   ],
   "source": [
    "a = [\"Apple\", \"Mango\", \"Banana\", \"Grapes\", 55, \"Apple\", 55]\n",
    "dup = []\n",
    "for x in a:\n",
    "    for i in dup:\n",
    "        if (x == i):\n",
    "            print('duplicate value is',x)\n",
    "    dup.append(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter key Name check if exist or not a\n",
      "Exist Key is Given\n"
     ]
    }
   ],
   "source": [
    "customer = {\n",
    "    'a': 4,\n",
    "    'b': 1,\n",
    "    'c': 6,\n",
    "    'd': 'apple'\n",
    "}\n",
    "check_keys =input(\"Enter key Name check if exist or not \")\n",
    "flag = False\n",
    "for i in customer.keys():\n",
    "    if i == check_keys:\n",
    "        flag = True\n",
    "        break\n",
    "if flag:\n",
    "    print(\"Exist Key is Given\")\n",
    "else:\n",
    "    print(\"Exist Key is not Given\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
