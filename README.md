<h1>H3lix Subdomain Enumerator</h1>
<p>This is a Python script that uses the SecurityTrails API to enumerate subdomains for a given domain.</p>
<h2>Prerequisites</h2>
<p>To run this script, you need:</p>
<ul>
  <li>Python 3.x</li>
  <li>The requests and termcolor Python modules</li>
</ul>
<p>Note that you need to replace YOUR_API_KEY_HERE with your actual SecurityTrails API key.</p>
<p>You can install the required modules using the pip package manager:</p>
<pre>pip install -r requirements.txt</pre>
<h2>Usage</h2>
<p>To run the script, use the following command:</p>
<pre>python h3lix_recon.py -d &lt;domain&gt;</pre>
<pre>python h3lix_recon.py -l &lt;filename&gt;</pre>
<p>Replace &lt;domain&gt; with the domain you want to enumerate subdomains for.</p>
<p>Replace &lt;filename&gt; with the file you want to enumerate subdomains for.</p>
<p>By default, this will save the list of subdomains to a file named &lt;domain&gt;_subdomains.txt.</p>
<h2>License</h2>
<p>The license for this script is not specified.</p>
