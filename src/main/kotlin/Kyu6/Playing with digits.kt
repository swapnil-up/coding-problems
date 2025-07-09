package Kyu6

import kotlin.math.pow

fun digPow(n: Int, p: Int): Int {
    var count=0
    var pow=p
    var digits=n.toString().map { it.toString().toInt() }
    var product=digits.sumOf { digit->
        val result=digit.toDouble().pow(pow+count).toInt()
        count++
        result
    }
    if (product%n==0) return product/n
    else return -1
}

fun main() {
    println(digPow(89, 1))
    println(digPow(92, 1))
    println(digPow(46288, 3))
}