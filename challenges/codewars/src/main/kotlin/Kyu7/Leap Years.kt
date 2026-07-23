package Kyu7

fun isLeapYear(year: Int) : Boolean {
    if (year%400==0) return true
    else if (year%100==0) return false
    else if (year%4==0) return true
    else return false
}

fun main() {
    println(isLeapYear(1234))
    println(isLeapYear(1984))
    println(isLeapYear(2000))
    println(isLeapYear(2010))
    println(isLeapYear(2013))
}