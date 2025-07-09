package Kyu7

fun getCount(str : String) : Int {
    var count=0
    for(i in 0 .. str.count()-1){
        if(str[i]== 'a'||str[i]== 'e'||str[i]== 'i'||str[i]== 'o'||str[i]== 'u') count+=1
    }
    return(count)
}
fun main(){
        println(getCount("abracadabra"))
        println(getCount("test"))
        println(getCount("example"))
}