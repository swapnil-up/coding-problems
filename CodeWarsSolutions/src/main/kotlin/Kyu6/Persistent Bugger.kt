package Kyu6

fun persistence(num: Int) : Int {
    var n=1
    var i=num
    if(num/10==0) return 0
    else{
        var count=0
        while(i/10!=0){
            while(i!=0){
                n=(i%10)*n
                i=i/10
            }
            i=n
            n=1
            count+=1
        }
        return count
    }
}

fun main() {
    println(persistence(39))
    println(persistence(4))
    println(persistence(25))
    println(persistence(999))
}