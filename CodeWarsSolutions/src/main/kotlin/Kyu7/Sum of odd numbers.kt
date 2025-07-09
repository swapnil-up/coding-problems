package Kyu7

fun rowSumOddNumbers(n: Int): Int {
    var sum=0
        for(j in n*(n-1)+1..n*(n+1)-1 step(2)){
            sum+=j
    }
    return sum
}

fun main() {
    println(rowSumOddNumbers(1))
    println(rowSumOddNumbers(2))
    println(rowSumOddNumbers(13))
    println(rowSumOddNumbers(19))
    println(rowSumOddNumbers(41))
    println(rowSumOddNumbers(42))
    println(rowSumOddNumbers(74))
    println(rowSumOddNumbers(86))
    println(rowSumOddNumbers(93))
    println(rowSumOddNumbers(101))
}