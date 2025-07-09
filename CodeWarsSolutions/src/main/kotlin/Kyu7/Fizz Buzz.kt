package Kyu7

fun fizzBuzz(n: Int): Array<String> {
    var arr= Array(n){""}
    for (i in 1..n){
        if (i %3==0 && i %5==0) arr[i-1]="FizzBuzz"
        else if (i %3==0) arr[i-1]="Fizz"
        else if (i %5==0) arr[i-1]="Buzz"
        else arr[i-1]=i.toString()
    }
    return arr
}

fun main() {
    val fizz= (fizzBuzz(10))
    for (element in fizz)
        println(element)
}