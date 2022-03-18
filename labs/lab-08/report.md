## Step 1:
![image](https://user-images.githubusercontent.com/66571652/159047153-d6d319ad-f253-4013-a369-2a7a44ca93d4.png)
![image](https://user-images.githubusercontent.com/66571652/159043880-02c21dc7-6864-4784-b59d-03655998b90d.png)

## Step 2:
- You can see what tests were run for a particular submission by clicking on the number underneath
the Fail/Pass/Not Run columns.
- https://open.cdash.org/test/645082657, Error condition is an outdated copyright, and this helps in debugging
the failure, as it shows the user has to update their copyright.
- https://open.cdash.org/build/7801794, The dashboard is very clean, 0 issues to be concerned with.
- https://open.cdash.org/viewTest.php?onlypassed&buildid=7802700. No errors.

![image](https://user-images.githubusercontent.com/66571652/159055596-cc7f3b20-28ef-4ed0-aeb3-7214900033e1.png)</br>
![image](https://user-images.githubusercontent.com/66571652/159055685-03874b24-5f77-4a20-9de4-bad41789dade.png)

## Step 3:
Testing provides details on the error using the flag --output-on-failure, where it states that the copyright year is incorrect (year is 2022 not 2020). </br>
![image](https://user-images.githubusercontent.com/66571652/159060177-ef968d1d-3769-4acc-abee-a7eb294e8879.png)</br>
Edited copyright year to have 2022 and remade in a new directory: </br>
![image](https://user-images.githubusercontent.com/66571652/159064508-afab5079-abd6-4afb-a9cd-930ce06afe0d.png)

## Step 4:

![image](https://user-images.githubusercontent.com/66571652/159069096-9bb7f852-052e-478a-8d0f-8ab0ae59507e.png) </br>
Repository with Test 5 example: https://github.com/jina2k/lab8test5example </br>
![image](https://user-images.githubusercontent.com/66571652/159078280-04dc4b33-1ab2-4102-9280-6301f3d5c875.png) </br>
![image](https://user-images.githubusercontent.com/66571652/159078351-1eca720c-a98c-4a7c-9721-2524a3cb694d.png)

