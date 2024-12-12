namespace Lab1_NenashevDM_6413;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        tabControl1 = new TabControl();
        tabPage1 = new TabPage();
        HuffmanDecode = new Button();
        label6 = new Label();
        label5 = new Label();
        label4 = new Label();
        label3 = new Label();
        Clear = new Button();
        HuffmanClick = new Button();
        Ratio = new TextBox();
        Decoded = new TextBox();
        Encoded = new TextBox();
        ProbabilitiesTextBox1 = new RichTextBox();
        OutputBox = new TextBox();
        InputBox = new TextBox();
        label2 = new Label();
        label1 = new Label();
        tabPage2 = new TabPage();
        ShennonFanoDecode = new Button();
        label7 = new Label();
        label8 = new Label();
        label9 = new Label();
        label10 = new Label();
        Clear1 = new Button();
        ShennonFanoClick = new Button();
        Ratio1 = new TextBox();
        Decoded1 = new TextBox();
        Encoded1 = new TextBox();
        ProbabilitiesTextBox2 = new RichTextBox();
        OutputBox1 = new TextBox();
        InputBox1 = new TextBox();
        label11 = new Label();
        label12 = new Label();
        tabPage3 = new TabPage();
        ArithmeticalDecode = new Button();
        label13 = new Label();
        label14 = new Label();
        label15 = new Label();
        label16 = new Label();
        Clear2 = new Button();
        ArithmeticalClick = new Button();
        Ratio2 = new TextBox();
        Decoded2 = new TextBox();
        Encoded2 = new TextBox();
        ProbabilitiesTextBox3 = new RichTextBox();
        OutputBox2 = new TextBox();
        InputBox2 = new TextBox();
        label17 = new Label();
        label18 = new Label();
        tabControl1.SuspendLayout();
        tabPage1.SuspendLayout();
        tabPage2.SuspendLayout();
        tabPage3.SuspendLayout();
        SuspendLayout();
        // 
        // tabControl1
        // 
        tabControl1.Controls.Add(tabPage1);
        tabControl1.Controls.Add(tabPage2);
        tabControl1.Controls.Add(tabPage3);
        tabControl1.Location = new Point(12, 12);
        tabControl1.Name = "tabControl1";
        tabControl1.SelectedIndex = 0;
        tabControl1.Size = new Size(1380, 755);
        tabControl1.TabIndex = 0;
        // 
        // tabPage1
        // 
        tabPage1.Controls.Add(HuffmanDecode);
        tabPage1.Controls.Add(label6);
        tabPage1.Controls.Add(label5);
        tabPage1.Controls.Add(label4);
        tabPage1.Controls.Add(label3);
        tabPage1.Controls.Add(Clear);
        tabPage1.Controls.Add(HuffmanClick);
        tabPage1.Controls.Add(Ratio);
        tabPage1.Controls.Add(Decoded);
        tabPage1.Controls.Add(Encoded);
        tabPage1.Controls.Add(ProbabilitiesTextBox1);
        tabPage1.Controls.Add(OutputBox);
        tabPage1.Controls.Add(InputBox);
        tabPage1.Controls.Add(label2);
        tabPage1.Controls.Add(label1);
        tabPage1.Location = new Point(4, 24);
        tabPage1.Name = "tabPage1";
        tabPage1.Padding = new Padding(3);
        tabPage1.Size = new Size(1372, 727);
        tabPage1.TabIndex = 0;
        tabPage1.Text = "Кодирование Хаффмана";
        tabPage1.UseVisualStyleBackColor = true;
        // 
        // HuffmanDecode
        // 
        HuffmanDecode.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        HuffmanDecode.Location = new Point(940, 340);
        HuffmanDecode.Name = "HuffmanDecode";
        HuffmanDecode.Size = new Size(159, 55);
        HuffmanDecode.TabIndex = 28;
        HuffmanDecode.Text = "Декодировать";
        HuffmanDecode.UseVisualStyleBackColor = true;
        HuffmanDecode.Click += HuffmanDecode_Click;
        // 
        // label6
        // 
        label6.AutoSize = true;
        label6.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label6.Location = new Point(87, 403);
        label6.Name = "label6";
        label6.Size = new Size(216, 25);
        label6.TabIndex = 27;
        label6.Text = "Порядок вероятностей";
        // 
        // label5
        // 
        label5.AutoSize = true;
        label5.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label5.Location = new Point(901, 551);
        label5.Name = "label5";
        label5.Size = new Size(128, 21);
        label5.TabIndex = 26;
        label5.Text = "Процент сжатия";
        // 
        // label4
        // 
        label4.AutoSize = true;
        label4.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label4.Location = new Point(901, 503);
        label4.Name = "label4";
        label4.Size = new Size(300, 21);
        label4.TabIndex = 25;
        label4.Text = "Объем закодированной строки в байтах";
        // 
        // label3
        // 
        label3.AutoSize = true;
        label3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label3.Location = new Point(901, 454);
        label3.Name = "label3";
        label3.Size = new Size(176, 21);
        label3.TabIndex = 24;
        label3.Text = "Объем строки в байтах";
        // 
        // Clear
        // 
        Clear.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        Clear.Location = new Point(1168, 340);
        Clear.Name = "Clear";
        Clear.Size = new Size(117, 55);
        Clear.TabIndex = 23;
        Clear.Text = "Очистить";
        Clear.UseVisualStyleBackColor = true;
        Clear.Click += Clear_Click;
        // 
        // HuffmanClick
        // 
        HuffmanClick.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        HuffmanClick.Location = new Point(775, 340);
        HuffmanClick.Name = "HuffmanClick";
        HuffmanClick.Size = new Size(159, 55);
        HuffmanClick.TabIndex = 22;
        HuffmanClick.Text = "Закодировать";
        HuffmanClick.UseVisualStyleBackColor = true;
        HuffmanClick.Click += HuffmanClick_Click;
        // 
        // Ratio
        // 
        Ratio.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Ratio.Location = new Point(662, 545);
        Ratio.Name = "Ratio";
        Ratio.Size = new Size(198, 33);
        Ratio.TabIndex = 21;
        // 
        // Decoded
        // 
        Decoded.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Decoded.Location = new Point(662, 497);
        Decoded.Name = "Decoded";
        Decoded.Size = new Size(198, 33);
        Decoded.TabIndex = 20;
        // 
        // Encoded
        // 
        Encoded.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Encoded.Location = new Point(662, 448);
        Encoded.Name = "Encoded";
        Encoded.Size = new Size(198, 33);
        Encoded.TabIndex = 19;
        // 
        // ProbabilitiesTextBox1
        // 
        ProbabilitiesTextBox1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        ProbabilitiesTextBox1.Location = new Point(87, 448);
        ProbabilitiesTextBox1.Name = "ProbabilitiesTextBox1";
        ProbabilitiesTextBox1.Size = new Size(362, 209);
        ProbabilitiesTextBox1.TabIndex = 18;
        ProbabilitiesTextBox1.Text = "";
        // 
        // OutputBox
        // 
        OutputBox.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        OutputBox.Location = new Point(463, 209);
        OutputBox.Name = "OutputBox";
        OutputBox.Size = new Size(471, 33);
        OutputBox.TabIndex = 17;
        // 
        // InputBox
        // 
        InputBox.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        InputBox.Location = new Point(463, 109);
        InputBox.Name = "InputBox";
        InputBox.Size = new Size(471, 33);
        InputBox.TabIndex = 16;
        // 
        // label2
        // 
        label2.AutoSize = true;
        label2.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label2.Location = new Point(662, 169);
        label2.Name = "label2";
        label2.Size = new Size(66, 37);
        label2.TabIndex = 15;
        label2.Text = "Код";
        // 
        // label1
        // 
        label1.AutoSize = true;
        label1.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label1.Location = new Point(662, 69);
        label1.Name = "label1";
        label1.Size = new Size(79, 37);
        label1.TabIndex = 14;
        label1.Text = "ФИО\r\n";
        // 
        // tabPage2
        // 
        tabPage2.Controls.Add(ShennonFanoDecode);
        tabPage2.Controls.Add(label7);
        tabPage2.Controls.Add(label8);
        tabPage2.Controls.Add(label9);
        tabPage2.Controls.Add(label10);
        tabPage2.Controls.Add(Clear1);
        tabPage2.Controls.Add(ShennonFanoClick);
        tabPage2.Controls.Add(Ratio1);
        tabPage2.Controls.Add(Decoded1);
        tabPage2.Controls.Add(Encoded1);
        tabPage2.Controls.Add(ProbabilitiesTextBox2);
        tabPage2.Controls.Add(OutputBox1);
        tabPage2.Controls.Add(InputBox1);
        tabPage2.Controls.Add(label11);
        tabPage2.Controls.Add(label12);
        tabPage2.Location = new Point(4, 24);
        tabPage2.Name = "tabPage2";
        tabPage2.Padding = new Padding(3);
        tabPage2.Size = new Size(1372, 727);
        tabPage2.TabIndex = 1;
        tabPage2.Text = "Кодирование Шеннона-Фано";
        tabPage2.UseVisualStyleBackColor = true;
        // 
        // ShennonFanoDecode
        // 
        ShennonFanoDecode.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        ShennonFanoDecode.Location = new Point(940, 340);
        ShennonFanoDecode.Name = "ShennonFanoDecode";
        ShennonFanoDecode.Size = new Size(159, 55);
        ShennonFanoDecode.TabIndex = 28;
        ShennonFanoDecode.Text = "Декодировать";
        ShennonFanoDecode.UseVisualStyleBackColor = true;
        ShennonFanoDecode.Click += ShennonFanoDecode_Click;
        // 
        // label7
        // 
        label7.AutoSize = true;
        label7.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label7.Location = new Point(87, 403);
        label7.Name = "label7";
        label7.Size = new Size(216, 25);
        label7.TabIndex = 27;
        label7.Text = "Порядок вероятностей";
        // 
        // label8
        // 
        label8.AutoSize = true;
        label8.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label8.Location = new Point(901, 551);
        label8.Name = "label8";
        label8.Size = new Size(128, 21);
        label8.TabIndex = 26;
        label8.Text = "Процент сжатия";
        // 
        // label9
        // 
        label9.AutoSize = true;
        label9.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label9.Location = new Point(901, 503);
        label9.Name = "label9";
        label9.Size = new Size(300, 21);
        label9.TabIndex = 25;
        label9.Text = "Объем закодированной строки в байтах";
        // 
        // label10
        // 
        label10.AutoSize = true;
        label10.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label10.Location = new Point(901, 454);
        label10.Name = "label10";
        label10.Size = new Size(176, 21);
        label10.TabIndex = 24;
        label10.Text = "Объем строки в байтах";
        // 
        // Clear1
        // 
        Clear1.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        Clear1.Location = new Point(1168, 340);
        Clear1.Name = "Clear1";
        Clear1.Size = new Size(117, 55);
        Clear1.TabIndex = 23;
        Clear1.Text = "Очистить";
        Clear1.UseVisualStyleBackColor = true;
        Clear1.Click += Clear1_Click;
        // 
        // ShennonFanoClick
        // 
        ShennonFanoClick.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        ShennonFanoClick.Location = new Point(775, 340);
        ShennonFanoClick.Name = "ShennonFanoClick";
        ShennonFanoClick.Size = new Size(159, 55);
        ShennonFanoClick.TabIndex = 22;
        ShennonFanoClick.Text = "Закодировать";
        ShennonFanoClick.UseVisualStyleBackColor = true;
        ShennonFanoClick.Click += ShennonFanoClick_Click;
        // 
        // Ratio1
        // 
        Ratio1.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Ratio1.Location = new Point(662, 545);
        Ratio1.Name = "Ratio1";
        Ratio1.Size = new Size(198, 33);
        Ratio1.TabIndex = 21;
        // 
        // Decoded1
        // 
        Decoded1.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Decoded1.Location = new Point(662, 497);
        Decoded1.Name = "Decoded1";
        Decoded1.Size = new Size(198, 33);
        Decoded1.TabIndex = 20;
        // 
        // Encoded1
        // 
        Encoded1.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Encoded1.Location = new Point(662, 448);
        Encoded1.Name = "Encoded1";
        Encoded1.Size = new Size(198, 33);
        Encoded1.TabIndex = 19;
        // 
        // ProbabilitiesTextBox2
        // 
        ProbabilitiesTextBox2.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        ProbabilitiesTextBox2.Location = new Point(87, 448);
        ProbabilitiesTextBox2.Name = "ProbabilitiesTextBox2";
        ProbabilitiesTextBox2.Size = new Size(362, 209);
        ProbabilitiesTextBox2.TabIndex = 18;
        ProbabilitiesTextBox2.Text = "";
        // 
        // OutputBox1
        // 
        OutputBox1.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        OutputBox1.Location = new Point(463, 209);
        OutputBox1.Name = "OutputBox1";
        OutputBox1.Size = new Size(471, 33);
        OutputBox1.TabIndex = 17;
        // 
        // InputBox1
        // 
        InputBox1.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        InputBox1.Location = new Point(463, 109);
        InputBox1.Name = "InputBox1";
        InputBox1.Size = new Size(471, 33);
        InputBox1.TabIndex = 16;
        // 
        // label11
        // 
        label11.AutoSize = true;
        label11.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label11.Location = new Point(662, 169);
        label11.Name = "label11";
        label11.Size = new Size(66, 37);
        label11.TabIndex = 15;
        label11.Text = "Код";
        // 
        // label12
        // 
        label12.AutoSize = true;
        label12.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label12.Location = new Point(662, 69);
        label12.Name = "label12";
        label12.Size = new Size(79, 37);
        label12.TabIndex = 14;
        label12.Text = "ФИО\r\n";
        // 
        // tabPage3
        // 
        tabPage3.Controls.Add(ArithmeticalDecode);
        tabPage3.Controls.Add(label13);
        tabPage3.Controls.Add(label14);
        tabPage3.Controls.Add(label15);
        tabPage3.Controls.Add(label16);
        tabPage3.Controls.Add(Clear2);
        tabPage3.Controls.Add(ArithmeticalClick);
        tabPage3.Controls.Add(Ratio2);
        tabPage3.Controls.Add(Decoded2);
        tabPage3.Controls.Add(Encoded2);
        tabPage3.Controls.Add(ProbabilitiesTextBox3);
        tabPage3.Controls.Add(OutputBox2);
        tabPage3.Controls.Add(InputBox2);
        tabPage3.Controls.Add(label17);
        tabPage3.Controls.Add(label18);
        tabPage3.Location = new Point(4, 24);
        tabPage3.Name = "tabPage3";
        tabPage3.Padding = new Padding(3);
        tabPage3.Size = new Size(1372, 727);
        tabPage3.TabIndex = 2;
        tabPage3.Text = "Арифметическое кодирование";
        tabPage3.UseVisualStyleBackColor = true;
        // 
        // ArithmeticalDecode
        // 
        ArithmeticalDecode.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        ArithmeticalDecode.Location = new Point(940, 340);
        ArithmeticalDecode.Name = "ArithmeticalDecode";
        ArithmeticalDecode.Size = new Size(159, 55);
        ArithmeticalDecode.TabIndex = 28;
        ArithmeticalDecode.Text = "Декодировать";
        ArithmeticalDecode.UseVisualStyleBackColor = true;
        ArithmeticalDecode.Click += ArithmeticalDecode_Click;
        // 
        // label13
        // 
        label13.AutoSize = true;
        label13.Font = new Font("Segoe UI Semibold", 14.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label13.Location = new Point(87, 403);
        label13.Name = "label13";
        label13.Size = new Size(216, 25);
        label13.TabIndex = 27;
        label13.Text = "Порядок вероятностей";
        // 
        // label14
        // 
        label14.AutoSize = true;
        label14.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label14.Location = new Point(901, 551);
        label14.Name = "label14";
        label14.Size = new Size(128, 21);
        label14.TabIndex = 26;
        label14.Text = "Процент сжатия";
        // 
        // label15
        // 
        label15.AutoSize = true;
        label15.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label15.Location = new Point(901, 503);
        label15.Name = "label15";
        label15.Size = new Size(300, 21);
        label15.TabIndex = 25;
        label15.Text = "Объем закодированной строки в байтах";
        // 
        // label16
        // 
        label16.AutoSize = true;
        label16.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        label16.Location = new Point(901, 454);
        label16.Name = "label16";
        label16.Size = new Size(176, 21);
        label16.TabIndex = 24;
        label16.Text = "Объем строки в байтах";
        // 
        // Clear2
        // 
        Clear2.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        Clear2.Location = new Point(1168, 340);
        Clear2.Name = "Clear2";
        Clear2.Size = new Size(117, 55);
        Clear2.TabIndex = 23;
        Clear2.Text = "Очистить";
        Clear2.UseVisualStyleBackColor = true;
        Clear2.Click += Clear2_Click;
        // 
        // ArithmeticalClick
        // 
        ArithmeticalClick.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 204);
        ArithmeticalClick.Location = new Point(775, 340);
        ArithmeticalClick.Name = "ArithmeticalClick";
        ArithmeticalClick.Size = new Size(159, 55);
        ArithmeticalClick.TabIndex = 22;
        ArithmeticalClick.Text = "Закодировать";
        ArithmeticalClick.UseVisualStyleBackColor = true;
        ArithmeticalClick.Click += ArithmeticalClick_Click;
        // 
        // Ratio2
        // 
        Ratio2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Ratio2.Location = new Point(662, 545);
        Ratio2.Name = "Ratio2";
        Ratio2.Size = new Size(198, 33);
        Ratio2.TabIndex = 21;
        // 
        // Decoded2
        // 
        Decoded2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Decoded2.Location = new Point(662, 497);
        Decoded2.Name = "Decoded2";
        Decoded2.Size = new Size(198, 33);
        Decoded2.TabIndex = 20;
        // 
        // Encoded2
        // 
        Encoded2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        Encoded2.Location = new Point(662, 448);
        Encoded2.Name = "Encoded2";
        Encoded2.Size = new Size(198, 33);
        Encoded2.TabIndex = 19;
        // 
        // ProbabilitiesTextBox3
        // 
        ProbabilitiesTextBox3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 204);
        ProbabilitiesTextBox3.Location = new Point(87, 448);
        ProbabilitiesTextBox3.Name = "ProbabilitiesTextBox3";
        ProbabilitiesTextBox3.Size = new Size(362, 209);
        ProbabilitiesTextBox3.TabIndex = 18;
        ProbabilitiesTextBox3.Text = "";
        // 
        // OutputBox2
        // 
        OutputBox2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        OutputBox2.Location = new Point(463, 209);
        OutputBox2.Name = "OutputBox2";
        OutputBox2.Size = new Size(471, 33);
        OutputBox2.TabIndex = 17;
        // 
        // InputBox2
        // 
        InputBox2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 204);
        InputBox2.Location = new Point(463, 109);
        InputBox2.Name = "InputBox2";
        InputBox2.Size = new Size(471, 33);
        InputBox2.TabIndex = 16;
        // 
        // label17
        // 
        label17.AutoSize = true;
        label17.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label17.Location = new Point(662, 169);
        label17.Name = "label17";
        label17.Size = new Size(66, 37);
        label17.TabIndex = 15;
        label17.Text = "Код";
        // 
        // label18
        // 
        label18.AutoSize = true;
        label18.Font = new Font("Segoe UI Semibold", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 204);
        label18.Location = new Point(662, 69);
        label18.Name = "label18";
        label18.Size = new Size(79, 37);
        label18.TabIndex = 14;
        label18.Text = "ФИО\r\n";
        // 
        // Form1
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(1404, 779);
        Controls.Add(tabControl1);
        Name = "Form1";
        Text = "Form1";
        tabControl1.ResumeLayout(false);
        tabPage1.ResumeLayout(false);
        tabPage1.PerformLayout();
        tabPage2.ResumeLayout(false);
        tabPage2.PerformLayout();
        tabPage3.ResumeLayout(false);
        tabPage3.PerformLayout();
        ResumeLayout(false);
    }

    #endregion

    private TabControl tabControl1;
    private TabPage tabPage1;
    private TabPage tabPage2;
    private TabPage tabPage3;
    private Label label6;
    private Label label5;
    private Label label4;
    private Label label3;
    private Button Clear;
    private Button HuffmanClick;
    private TextBox Ratio;
    private TextBox Decoded;
    private TextBox Encoded;
    private RichTextBox ProbabilitiesTextBox1;
    private TextBox OutputBox;
    private TextBox InputBox;
    private Label label2;
    private Label label1;
    private Label label7;
    private Label label8;
    private Label label9;
    private Label label10;
    private Button Clear1;
    private Button ShennonFanoClick;
    private TextBox Ratio1;
    private TextBox Decoded1;
    private TextBox Encoded1;
    private RichTextBox ProbabilitiesTextBox2;
    private TextBox OutputBox1;
    private TextBox InputBox1;
    private Label label11;
    private Label label12;
    private Label label13;
    private Label label14;
    private Label label15;
    private Label label16;
    private Button Clear2;
    private Button ArithmeticalClick;
    private TextBox Ratio2;
    private TextBox Decoded2;
    private TextBox Encoded2;
    private RichTextBox ProbabilitiesTextBox3;
    private TextBox OutputBox2;
    private TextBox InputBox2;
    private Label label17;
    private Label label18;
    private Button HuffmanDecode;
    private Button ShennonFanoDecode;
    private Button ArithmeticalDecode;
}
