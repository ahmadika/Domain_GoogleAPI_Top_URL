Design thoughts about the package
====

*This is a list of design thoughts that have appeared in building/modifying this package and their provisional resolution. They should be taken as useful indicators of what was the developer maintaining this package thinking when making design decisions.*

* **Relocating methods of public Google class in separated modules** The idea is to encapsulate the logic and functions of each kind of search method outside the public class used by the user to be able to maintain them on an individual basis and repair them without touching the main module and its interface. (Is this more maintainable or is overkilling the problem?)
    - As the project may grow or the logic of the used methods may change, it is more maintainable to modularize. This shouldn't add more complication to the package since developers are used to deal with many files, if the structure of the modules make sense.

* **Duplicated docstrings between methods in the main class and methods in the modules** Updates in main module (google) docstrings should be followed by duplicated updates in auxiliary module's docstrings. (Should I put docstrings only in the main module or manage both, even in a duplicated basis?)
    - It is better to make the methods in the main public module be just a reference to the methods hold in the auxiliary modules, so only docstrings and signature of the method written in the module need to be taken care.

* **Private methods "floating" in a module as global methods** It feels uncomfortable to have private methods not wrapped into a class, but adding classes inside auxiliary methods complicates the interface of the modules unnecessarily (should I keep them like this? Without putting them inside "wrapping" classes?)
    - There is nothing wrong about having public and private methods in a module. The most important thing here is to build a clear user interface for the module.

* **Order of methods in the modules** Private methods before public methods or vice-versa? First approach shows the bricks of the wall first, and then the wall. The second approach shows first the methods that are expected to be used by the user, delaying the reading of some implementation details.
    - I'm not really sure about the convenience of one approach over the other one. Provisionally I'm taking the second approach as the better one, because I thing could improve readability.

* **Top down approach in currency: overkilling?** How far would be desirable to go in breaking down public methods into private ones to make more clear the algorithm followed by the main public method?
    - Making private methods with declarative names shows clearer algorithms, encapsulate issues than therefore can be dealt separately and avoid the need of in-line comments. Although tightly related private methods may not be separated, if it's unclear that they can truly be dealt separately.

* **Closely related tests between main module and auxiliary modules** Some tests in the google module seems to test just the same than some tests in the auxiliary modules. At some point this is duplicating code and work (specially when test must be changed) but they respond to different compartments of the package.
    - I am not really sure about the subject. The safest approach would be to say that those tests are really testing different things, even if the tests of the main class are just testing that the reference to the methods written inside auxiliary classes are working fine.

* **Is it ok to upload something so informal as these DESIGN_THOUGHTS to Github?** Is this the proper place to state these thoughts? Are these thoughts something I should rather keep to myself in a private file?
    - The design thoughts that a developer has when building a package (even, as is this case, with a newbie developer) can be useful for someone to understand, improve or discuss any productive changes that can be made in the package. They may sound silly sometimes, they may be even just totally wrong, but they offer (I think) a quick insight on what was this person thinking when taking these design decisions.