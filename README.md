# Chapter 20


## Question 1

## Question 2

## Question 3

## Question 4

## Question 5

## Question 6




# Chapter 21
## Question 1
**user time** column value changes to 50 when running 1 instance of mem. It goes to 100 when running 2 instances.
## Question 2
the amount of free memory sometimes increases quite a lot after the program exits.

## Question 3

./mem 2048
allocating 2147483648 bytes (2048.00 MB)
  number of integers in array: 536870912
loop 0 in 3145.17 ms (bandwidth: 651.16 MB/s)
loop 1 in 34464.27 ms (bandwidth: 59.42 MB/s)


first loop is a faster than the subsuquent loops. 


procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 3  0 1057024  71728      0  23860 69000 62384 69152 62384 2812 4709  1  5 37 57  0
 0  2 1065216  75524      0  23776 64696 72312 64696 72312 2754 4492  1  6 32 62  0
 0  1 1069568  80564      0  24292 61592 66172 62196 66172 2547 4203  1  4 34 61  0
 0  2 1067520  72200      0  28552 63988 61832 71864 61832 3857 6257  2  5 21 71  0
 0  2 1098240  96628      0  35072 45176 76456 53192 76456 2511 3875  1  6 19 75  0
 0  1 1077504  76208      0  36280 66748 46184 76080 46184 2955 4978  1  4 32 62  0
 0  1 1076224  83012      0  33736 66048 65328 66048 65330 2710 4461  2  4 31 64  0
 2  1 1035776  71720      0  30840 79104 51012 79104 51012 3130 5350  2  4 43 51  0
 0  1 949504  65132      0  25448 87568 39236 87568 39296 3104 5692  1  6 44 47  2
 0  1 937728  60596      0  24960 74880 67612 75708 67612 2886 4978  1  7 39 53  0
 0  1 932352  67936      0  24820 67368 69984 67720 69984 2688 4616  2  6 43 50  0
 0  2 947968  76252      0  24312 60512 71684 60512 71684 2429 4081  0  9 36 55  0
 0  2 972800  65872      0  24360 60704 67840 60704 67840 2415 4058  2  6 32 60  0
 0  1 984832  62580      0  24212 62784 65192 62784 65194 2492 4206  1  7 39 53  0
 0  2 992000  61068      0  24792 65600 70588 66216 70728 2640 4497  1  5 41 53  0
 0  1 1018624  65564      0  24788 56096 69824 56096 69824 2315 3793  1  6 35 58  0
 0  1 1048320  63532      0  24732 58144 71396 58144 71396 2347 3911  1  6 36 58  0

## Question 4
When swap is on use, block I/O increases and cpu usage decreases as the process is bottlenecked by I/O.
## Question 5
![bandwidth](./bandwidth.png)
![loops](./loops.png)


## Question 6
memory allocation fails at 4000 in my 2GB RAM+2GB Swap configuration.


## Question 7

Swap will be faster on SSDs than HDD. NVMe SSDs will perform better than SATA SSDs.




# Chapter 22
## Question 1

## Question 2

## Question 3

## Question 4

## Question 5

## Question 6
