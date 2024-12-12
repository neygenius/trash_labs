namespace Lab1_NenashevDM_6413;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
    }

    private void HuffmanClick_Click(object sender, EventArgs e)
    {
        ProbabilitiesTextBox1.Clear();
        string inputText = InputBox.Text;

        var huffman = new HuffmanAlgorithm();
        var codes = huffman.Encode(inputText);
        string encodedText = string.Join("", inputText.Select(c => codes[c]));

        // Вывод закодированного текста
        OutputBox.Text = encodedText.ToString();

        // Вывод вероятностей
        ProbabilitiesTextBox1.Clear();
        var frequencies = inputText.GroupBy(c => c).ToDictionary(g => g.Key, g => (double)g.Count() / inputText.Length);
        foreach (var kvp in frequencies)
        {
            ProbabilitiesTextBox1.AppendText($"{kvp.Key}: {kvp.Value:P} - {codes[kvp.Key]}\n");
        }

        // Вывод размеров и коэффициента сжатия
        int originalSize = inputText.Length * 8; // Размер в битах
        int encodedSize = encodedText.Length;    // Размер в битах

        Encoded.Text = originalSize.ToString(); //Размер в битах
        Decoded.Text = encodedSize.ToString();  //Размер в битах

        double compressionRatio = (1 - (double)encodedSize / originalSize) * 100;
        Ratio.Text = $"{compressionRatio:F2}%";
    }

    private void HuffmanDecode_Click(object sender, EventArgs e)
    {
        string inputText = InputBox.Text;
        InputBox.Clear();

        var huffman = new HuffmanAlgorithm();
        var codes = huffman.Encode(inputText);
        string encodedText = string.Join("", inputText.Select(c => codes[c]));

        string decodedText = huffman.Decode(encodedText);

        InputBox.Text = decodedText;
    }

    private void Clear_Click(object sender, EventArgs e)
    {
        if (string.IsNullOrEmpty(InputBox.Text))
            return;
        InputBox.Clear();
        OutputBox.Clear();
        Encoded.Clear();
        Decoded.Clear();
        Ratio.Clear();
        ProbabilitiesTextBox1.Clear();
    }

    private void ShennonFanoClick_Click(object sender, EventArgs e)
    {
        ProbabilitiesTextBox2.Clear();
        string inputText = InputBox1.Text;

        var shannonFano = new ShannonFanoAlgorithm();
        string encodedText = shannonFano.Encode(inputText);

        // Вывод закодированного текста
        OutputBox1.Text = encodedText;

        // Вывод вероятностей
        var frequencies = inputText.GroupBy(c => c).ToDictionary(g => g.Key, g => (double)g.Count() / inputText.Length);
        foreach (var freq in frequencies)
        {
            ProbabilitiesTextBox2.AppendText($"{freq.Key}: {freq.Value:P}\n");
        }

        // Вывод размеров и коэффициента сжатия (исправленный расчет)
        int originalSize = inputText.Length * 8; // Размер в битах
        int encodedSize = encodedText.Length;    // Размер в битах

        Encoded1.Text = originalSize.ToString();
        Decoded1.Text = encodedSize.ToString();

        double compressionRatio = (1 - (double)encodedSize / originalSize) * 100;
        Ratio1.Text = $"{compressionRatio:F2}%";
    }

    private void ShennonFanoDecode_Click(object sender, EventArgs e)
    {
        string inputText = InputBox1.Text;
        InputBox1.Clear();

        var shannonFano = new ShannonFanoAlgorithm();
        string encodedText = shannonFano.Encode(inputText);
        string decodedText = shannonFano.Decode(encodedText);

        // Вывод закодированного текста
        InputBox1.Text = decodedText;
    }

    private void Clear1_Click(object sender, EventArgs e)
    {
        if (string.IsNullOrEmpty(InputBox1.Text))
            return;
        InputBox1.Clear();
        OutputBox1.Clear();
        Encoded1.Clear();
        Decoded1.Clear();
        Ratio1.Clear();
        ProbabilitiesTextBox2.Clear();
    }

    private void ArithmeticalClick_Click(object sender, EventArgs e)
    {
        ProbabilitiesTextBox3.Clear();
        string inputText = InputBox2.Text;

        var arithmetical = new ArithmeticalAlgorithm();
        string encodedText = arithmetical.Encode(inputText);
        OutputBox2.Text = encodedText;

        // Вывод вероятностей
        ProbabilitiesTextBox3.Clear();
        var frequencies = inputText.GroupBy(c => c).ToDictionary(g => g.Key, g => (double)g.Count() / inputText.Length);
        foreach (var freq in frequencies)
        {
            ProbabilitiesTextBox3.AppendText($"{freq.Key}: {freq.Value:P}\n");
        }

        // Вывод размеров и коэффициента сжатия
        int originalSize = inputText.Length * 8; // Размер в битах
        int encodedSize = encodedText.Length; // Приблизительный размер в символах (не битах!)

        Encoded2.Text = originalSize.ToString();
        Decoded2.Text = encodedSize.ToString();

        // Используем приблизительный размер в символах, так как точный размер в битах неизвестен без бинарного представления.
        double compressionRatio = (1 - (double)encodedSize / originalSize) * 100;
        Ratio2.Text = $"{compressionRatio:F2}%";
    }

    private void ArithmeticalDecode_Click(object sender, EventArgs e)
    {
        string inputText = InputBox2.Text;
        InputBox2.Clear();

        var arithmetical = new ArithmeticalAlgorithm();
        string encodedText = arithmetical.Encode(inputText);
        string decodedText = arithmetical.Decode(encodedText, inputText.Length);

        InputBox2.Text = decodedText;
    }

    private void Clear2_Click(object sender, EventArgs e)
    {
        if (string.IsNullOrEmpty(InputBox2.Text))
            return;
        InputBox2.Clear();
        OutputBox2.Clear();
        Encoded2.Clear();
        Decoded2.Clear();
        Ratio2.Clear();
        ProbabilitiesTextBox3.Clear();
    }
        
}
