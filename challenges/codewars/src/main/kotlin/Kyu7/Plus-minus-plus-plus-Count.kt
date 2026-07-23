package Kyu7

fun catchSignChange(arr: Array<Int>): Int {
    var count=0
    for (i in 0..arr.size-2){
        if (arr[i]>=0 &&arr[(i+1)]<0) count++
        if (arr[i]<0 &&arr[(i+1)]>=0) count++

    }
    return count
}
//if (arr[i]==0 ||arr.last()==0) count--

fun main() {
    println(catchSignChange(arrayOf(1, 3, 4, 5)));
    println(catchSignChange(arrayOf<Int>()));
    println(catchSignChange(arrayOf(1, -3, -4, 0, 5)));
    println(catchSignChange(arrayOf(-47,84,-30,-11,-5,74,77)));
    println(catchSignChange(arrayOf(0, 65, 34, -188, 123, 91, -154, 7, 45, -91, 178, 110, 100, -177, -15, -139, -96, -190, -19)));
}