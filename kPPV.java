package kppv;

import java.io.*;

/**
 * @author hubert.cardot
 */
public class kPPV {
    static int NbEx=50, NbClasse=3, NbCaract=4, NbExApprent=25;
    static Double data[][][] = new Double[NbClasse][NbEx][NbCaract];

    public static void main(String[] args) {
        System.out.println("Début programme kPPV");
        lectureFichier();

        Double X[] = new Double[NbCaract];
        Double Dist[] = new Double[NbClasse*NbExApprent];

        //A faire...

    }
    private static void calculDistances(Double X[], Double Dist[]) {
        //---calcule la distance entre l'ex. X et tous les ex. d'apprentissage

        // A faire...
    }
    private static void lectureFichier() {
        //---lecture des données à partir du fichier iris.data
        String ligne, sousChaine;
        int classe=0, n=0;
        try {
             BufferedReader fic=new BufferedReader(new FileReader("iris.data"));
             while ((ligne=fic.readLine())!=null) {
                for(int i=0;i<NbCaract;i++) {
                    sousChaine = ligne.substring(i*NbCaract, i*NbCaract+3);
                    data[classe][n][i] = Double.parseDouble(sousChaine);
                    System.out.println(data[classe][n][i]+" "+classe+" "+n);
                }
                if (++n==NbEx) { n=0; classe++; }
             }
        }
        catch (Exception e) { System.out.println(e.toString()); }
    }

} //fin classe kPPV
