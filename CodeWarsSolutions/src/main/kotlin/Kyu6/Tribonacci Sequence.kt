package Kyu6

fun tribonacci(signature: DoubleArray, n: Int): DoubleArray {
    var tri= mutableListOf<Double>()
    for (i in 0..2){
        tri.add(signature[i])
    }
    for (i in 3..n-1){
        tri.add(tri[i-1]+tri[i-2]+tri[i-3])
    }
    return tri.toDoubleArray()
}

fun main() {
    val result1 = tribonacci(doubleArrayOf(1.0, 1.0, 1.0), 10)
    val result2 = tribonacci(doubleArrayOf(0.0, 0.0, 1.0), 10)
    val result3 = tribonacci(doubleArrayOf(0.0, 1.0, 1.0), 10)

    println(result1.joinToString(", ")) // Print the values as a comma-separated string
    println(result2.joinToString(", "))
    println(result3.joinToString(", "))
}