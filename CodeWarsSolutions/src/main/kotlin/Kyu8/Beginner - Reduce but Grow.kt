package Kyu8

fun grow(arr: IntArray): Int {
    var result=1
    for (i in 0..arr.size-1){
        result*=arr[i]
    }
    return result
}

fun main() {
    println(grow(intArrayOf(1, 2, 3)))
    println(grow(intArrayOf(4, 1, 1, 1, 4)))
    println(grow(intArrayOf(2, 2, 2, 2, 2, 2)))
}