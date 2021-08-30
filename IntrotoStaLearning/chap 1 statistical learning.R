# Title     : chap1 intro to R
# Objective : practice R codes
# Created by: lihanwei
# Created on: 10.3.2021
x = c(1,6,2) # c() to create a vector of numbers, for concatenate
y = c(1,4,3)
length(x)
length(y)
x+y
ls() #look at a list of all the objects.
rm() # delete any that we don'' want
rm(x,y)
ls()
rm(list=ls()) # remove all objects at once
?matrix() # create a matrix of numbers
x = matrix(data=c(1,2,3,4),nrow=2, ncol=2)
# to create a matrice by filling in order of the rows
x = matrix(data=c(1,2,3,4),nrow=2,ncol=2,byrow = TRUE)
ls()
sqrt(x) # returns the square root of each element of a vector or matrix.

x^2# raise each element of x to the power of 2

x = rnorm(50) #rnorm() function generates a vector of random normal variables,
# with first argument n the sample size.
y = x+rnorm(50,mean = 50,sd=.1)
x
y
cor(x,y) # correlation

set.seed(2) #create a set of random numbers that can be reproduced.
rnorm(49) # after the set.seed() function, the rnorm will produce the same set of
# random variables that is involved to the seed number.
set.seed(3)
y = rnorm(100)
mean(y) #mean of a vector of numbers
var(y) # variance of a vector of numbers
sqrt(var(y))
sd(y) #standard deviation of the variable


x = rnorm(100)
y = rnorm(100)
x
y
?plot()
plot(x,y) #the primary way of plot data in R.
plot(x,y,xlab="x-axis",ylab="y-axis",main='plot of X vs Y')
# pdf("Figure.pdf") #save the output of an R plot
plot(x,y,col = )
dev.off() #indicates that we are done creating the plot.

seq(0,1,length=10) #makes a sequence of 10 numbersthat are equally spaced between 0 and 1
x=seq(1,10)
x=1:10 #shorthand for seq(3,10)
x = seq(-pi,pi,length=50)
x

# contour() function produces a contour plot to represent three-dimensional data,
# like a topographical map. A vector of x values. A vector of the y values.
# a matrix whose elements correspond to the z value.
y=x
f=outer(x,y,function(x,y)cos(y)/(1+2^2))
contour(x,y,f)
contour(x,y,f,nlevels = 45,add=T)
fa=(f-t(f)/2)
contour(x,y,fa,nlevels=15)

image(x,y,fa) #color-coded plot whose colors depend on the z value
persp(x,y,fa) #produce a three-dimensional plot
persp(x,y,fa,theta=30)
persp(x,y,fa,theta=20,phi=20)
persp(x,y,fa,theta=20,phi=20)
persp(x,y,fa,theta=30,phi=40)

A = matrix(1:16,4,4)
A
A[2,3] #select the second row and the third coloumn
A[c(1,3),c(2,4)] #first row third coloumn ; second row fourth coloumn
A[1:3,2:4] # first to third row, second to fourth coloumn
A[1:2,] #first to second row
A[,1:2] #first to second colomn

A[-c(1,3),] #keep all rows or columns except those indicated in the index
A[-c(1,3),-c(1,3,4)]

dim(A) # the number of rows, the number of columns of any given matrix

# Loading data
Auto = read.table("/Users/lihanwei/PycharmProjects/untitled/IntrotoStaLearning/Auto.data") #import a dataset into R
fix(Auto) #view in a spreadsheet like window

