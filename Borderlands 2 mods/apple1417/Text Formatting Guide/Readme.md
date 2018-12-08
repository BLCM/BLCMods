### Text Formatting
This guide's going to look at how item or skill descriptions are formatted, and how you can add your own, completely new, custom formats.

The formatting is all based on a stripped down version of html. It's pure html, there's no css/javascript support, and only a very small subset of tags actually do anything. Tags with known effects are:
- `<!-- -->` - Properly comments out text, kind of useless
- `<!--` - Without an end tag a comment crashes the game when it tries to render it
- `<br>` - Adds newlines as expected
- `<font>` - The size and colour attributes work as expected, but face can probably only ever select the default font making it useless
- `<p>` - Adds newlines as expected
- `<u>` - Adds a one-pixel tall underline without a border.
- `< -/>` - For some reason this causes everything that's supposed to render after it to disappear.

You can insert any of these into standard text fields to get their formatting

#### Custom Tags
If you go look through object dumps you'll pretty much never see raw html used. Instead you'll see something like the following:

```
*** Property dump for object 'SkillDefinition GD_Tulip_Mechromancer_Skills.LittleBigTrouble.LightningStrike' ***
=== SkillDefinition properties ===
...
SkillDescription=[skill]Deathtrap Ability[-skill].  Deathtrap charges his blades with electricity and attacks an enemy dealing [shock]Shock Damage[-shock].
```

These custom tags are much more readable, so if you're going to format a lot of text you should use them instead.

The custom tags are converted to html through a dictionary stored in `TextMarkupDictionary'GD_Globals.UI.TheTextMarkupDictionary'`. Each entry is in the following format:

```
Dictionary(7)=
(
    MarkupTag = "skill",
    HTMLMarkupBeginText = "<font color="#FFDEAD"><i>",
    HTMLMarkupEndText = "</i></font>",
    MarkupBeginTag = "[skill]",
    MarkupEndTag = "[-skill]"
)
```
Note that the `<i>` tag doesn't actually have an effect.

When the game renders text it looks for MarkupBeginTags and MarkupEndTags, and replaces them with the relevant HTMLMarkupBeginText or HTMLMarkupEndText. Not only can you setup your html tags in them, you can also just add plaintext prefixes or suffixes.

Unfortunately editing this dictionary isn't quite as simple as most things in the game. If you just try set a new value for the whole array all the MarkupBeginTags and MarkupEndTags will be blank, leading to nothing being formatted. You have to add hotfixes fixing all these values alongside the set command. to get everything to work.

#### Example
In this folder there is an example mod, `TextFormattingDemo.blcm`, showing off how you might setup your own formatting. It edits the red text on the rapier, using both methods. It is a bit of an extreme example, so it will cause the game to lag when you try read it, but your mods almost certainly won't add as much text so it won't be an issue with them.
