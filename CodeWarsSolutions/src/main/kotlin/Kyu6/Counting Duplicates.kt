package Kyu6

fun duplicateCount(text: String): Int {
    if(text.count()>text.lowercase().toCharArray().distinct().count())
        return(text.lowercase().groupingBy { it }.eachCount().filter { it.value>1 }.count())
    else return(0)
}

fun main() {
    println(duplicateCount("abcde"))
    println(duplicateCount("abcdea"))
    println(duplicateCount("indivisibility"))
    val text = "dA" + "c".repeat(10) + "b".repeat(100) + "a".repeat(1000)
    println(duplicateCount(text))
}

