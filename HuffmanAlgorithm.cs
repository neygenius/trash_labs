using System.Text;

namespace Lab1_NenashevDM_6413;

public class HuffmanAlgorithm
{
    private class Node
    {
        public char? Character { get; set; }
        public double Frequency { get; set; }
        public Node? Left { get; set; }
        public Node? Right { get; set; }

        public Node(char? character, double frequency, Node? left = null, Node? right = null)
        {
            Character = character;
            Frequency = frequency;
            Left = left;
            Right = right;
        }
    }

    private Dictionary<char, string> codes = new Dictionary<char, string>();
    private Node? root;

    public Dictionary<char, string> Encode(string input)
    {
        var probabilities = GetFrequencies(input);
        root = BuildHuffmanTree(probabilities);
        GenerateCodes(root, "");

        return codes;
    }

    public string Decode(string encodedString)
    {
        if (root == null)
        {
            throw new InvalidOperationException("Дерево Хаффмана не было инициализировано.");
        }

        var currentNode = root;
        var decodedString = new StringBuilder();

        foreach (char bit in encodedString)
        {
            currentNode = bit == '0' ? currentNode?.Left : currentNode?.Right;

            if (currentNode != null && currentNode.Character.HasValue)
            {
                decodedString.Append(currentNode.Character.Value);
                currentNode = root; // Возвращаемся к корню
            }
        }

        return decodedString.ToString();
    }

    private Dictionary<char, double> GetFrequencies(string input)
    {
        return input.GroupBy(c => c).ToDictionary(g => g.Key, g => (double)g.Count() / input.Length);
    }

    private Node? BuildHuffmanTree(Dictionary<char, double> frequencies)
    {
        var nodes = frequencies.Select(kvp => new Node(kvp.Key, kvp.Value)).ToList();

        while (nodes.Count > 1)
        {
            nodes = nodes.OrderBy(n => n.Frequency).ToList();
            var left = nodes[0];
            var right = nodes[1];
            var parent = new Node(null, left.Frequency + right.Frequency, left, right);
            nodes.RemoveAt(0);
            nodes.RemoveAt(0);
            nodes.Add(parent);
        }

        return nodes.FirstOrDefault();
    }

    private void GenerateCodes(Node? node, string currentCode)
    {
        if (node == null) return;

        if (node.Character.HasValue)
        {
            codes[node.Character.Value] = currentCode;
            return;
        }

        GenerateCodes(node.Left, currentCode + "0");
        GenerateCodes(node.Right, currentCode + "1");
    }
}
