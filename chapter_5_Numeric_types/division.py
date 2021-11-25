#Python is a dynamically-typed language, so there is no declaration of function or parameter types. In the function signature, you see no type requirements at all.
#Classic Division:  Truncating results for integers ,and keeping reminders (i.e. fractional parts) for floating point numbers.
# অপারেন্ড(operand) ইন্টিজার(interger) হলে রিমাইন্ডার(reminder) টুকু বাদ দিয়ে দেয় । ;  (That was exist in python 2.0X ,no existence in python 3.0X)
#True Division: Always keeping reminders in floating floating point results ,regardless of types.
#Floor Division: Always Truncates fractional reminders down to their floor ,regardless of types .It result type depend on the type of it's operands.

# Division: Classic ,Floor and Ture :পাইথন ২।০ তে '/'অপারেটর কে দুইটির যেকোনো এক্টি সংখ্যা ফ্লোটিং পয়েন্ট দিলে পয়েন্টের পরের অংশগুলো রেখে দেয় (7/2.0 =7.0/2=7.0/2.0 =3.5) । আর দুইটি সংখ্যাই ইন্টিজার দিলে শুদুমাত্র ইন্টিজার
# অংশটুকু প্রিন্ট করে ,দশমিকের পরে অংশটুকু প্রিন্ট করে না।7/2= 3 (but 3.5 in real life) এট ক্লাসিক ডিভিশন
# কিন্তু পাইথন ৩ এ / অপারেটর সবসময় দশমিক এর পরের অংশটুকু রেখে দেয় ইনপুট হিসেবে ইন্টিজার দেয়া হোক বা ফ্লোটিং পয়েন্ট দেয়া হোক ।(7/2=7/2.0 =7.0/2=7.0/2.0 =3.5)
#"//" do same tasks on python 3.0X and 2.0X ---this operator returns only floor value of a division if i use any operand as floating point the result will be floating point otherwise
#resutl will be integer(7/2=3 ;7.0/2=3.0);data type of the result for // is still dependent on the operand types in 3.X : if either is float the result is float ;otherwise ,it is an
#integer.

# --------------------------------------Examples----------------------------------------------------
print(10/4)
print(10/4.0)
print(10//4)
print(10//4.0)


#------------------------------------------in python that would be------------------------------
# 10/4=2
# 10/4.0=2.5
# 10//4=2
# 10/4.0=2.0---





