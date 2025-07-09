package Kyu6

fun solution(number: Int): Int {
    var sum=0
    for(i in 0..<number){
        if (i%3==0 ||i%5==0) sum+=i
    }
    return sum
}

fun main() {
    println(solution(10))
    println(solution(20))
    println(solution(200))
}