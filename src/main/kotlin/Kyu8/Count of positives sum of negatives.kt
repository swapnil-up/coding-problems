package Kyu8

fun countPositivesSumNegatives(input : Array<Int>?) : Array<Int>? {
    var sumneg=0
    var countpos=0
    input?.forEach {
        when {
            it < 0 -> sumneg -= -it
            it > 0 -> countpos++
        }
    }
    if (countpos==0 && sumneg==0) return emptyArray()
    return arrayOf(countpos,sumneg)
}

fun main() {
    println(countPositivesSumNegatives(arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15)))
    println(countPositivesSumNegatives(arrayOf(0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14)))
}