
public class BubbleSort {
    public static void bubbleSort(int a[]){
        for (int i=0; i<a.length; i++){
            for (int j=0; j<a.length-1; j++){
                if(a[j]>a[j+1]){
                    int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
    }
    public static void main(String args[]){
        int a[]={7,2,5,4,1,3};
        bubbleSort(a);
        for (int i : a)
            System.out.print(i+" ");
    }
}
