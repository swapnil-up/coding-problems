package Kyu7

fun smallEnough(a : IntArray, limit : Int) : Boolean {
    for (i in 0..a.size-1){
        if (a[i]>limit) return false
    }
    return true
}

fun main() {
    println(smallEnough(intArrayOf(66, 101), 200))
    println(smallEnough(intArrayOf(78, 117, 110, 99, 104, 117, 107, 115), 100))
    println(smallEnough(intArrayOf(101, 45, 75, 105, 99, 107), 107))
    println(smallEnough(intArrayOf(80, 117, 115, 104, 45, 85, 112, 115), 120))
}