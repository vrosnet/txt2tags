"""
A Lout target.
http://savannah.nongnu.org/projects/lout
Target specific occurrence number in txt2tags core: 3.
"""

NAME = 'Lout document'

TYPE = 'office'

HEADER = """\
@SysInclude { doc }
@Document
  @InitialFont { Times Base 12p }  # Times, Courier, Helvetica, ...
  @PageOrientation { Portrait }    # Portrait, Landscape
  @ColumnNumber { 1 }              # Number of columns (2, 3, ...)
  @PageHeaders { Simple }          # None, Simple, Titles, NoTitles
  @InitialLanguage { English }     # German, French, Portuguese, ...
  @OptimizePages { Yes }           # Yes/No smart page break feature
//
@Text @Begin
@Display @Heading { %(HEADER1)s }
@Display @I { %(HEADER2)s }
@Display { %(HEADER3)s }
#@NP                               # Break page after Headers
"""

TAGS = {
    'paragraphOpen'        : '@LP'                     ,
    'blockTitle1Open'      : '@BeginSections'          ,
    'blockTitle1Close'     : '@EndSections'            ,
    'blockTitle2Open'      : ' @BeginSubSections'      ,
    'blockTitle2Close'     : ' @EndSubSections'        ,
    'blockTitle3Open'      : '  @BeginSubSubSections'  ,
    'blockTitle3Close'     : '  @EndSubSubSections'    ,
    'title1Open'           : '~A~@Section @Title { \a } @Begin',
    'title1Close'          : '@End @Section'           ,
    'title2Open'           : '~A~ @SubSection @Title { \a } @Begin',
    'title2Close'          : ' @End @SubSection'       ,
    'title3Open'           : '~A~  @SubSubSection @Title { \a } @Begin',
    'title3Close'          : '  @End @SubSubSection'   ,
    'title4Open'           : '~A~@LP @LeftDisplay @B { \a }',
    'title5Open'           : '~A~@LP @LeftDisplay @B { \a }',
    'anchor'               : '@Tag { \a }\n'       ,
    'blockVerbOpen'        : '@LP @ID @F @RawVerbatim @Begin',
    'blockVerbClose'       : '@End @RawVerbatim'   ,
    'blockQuoteOpen'       : '@QD {'               ,
    'blockQuoteClose'      : '}'                   ,
    # enclosed inside {} to deal with joined**words**
    'fontMonoOpen'         : '{@F {'               ,
    'fontMonoClose'        : '}}'                  ,
    'fontBoldOpen'         : '{@B {'               ,
    'fontBoldClose'        : '}}'                  ,
    'fontItalicOpen'       : '{@II {'              ,
    'fontItalicClose'      : '}}'                  ,
    'fontUnderlineOpen'    : '{@Underline{'        ,
    'fontUnderlineClose'   : '}}'                  ,
    # the full form is more readable, but could be BL EL LI NL TL DTI
    'listOpen'             : '@BulletList'         ,
    'listClose'            : '@EndList'            ,
    'listItemOpen'         : '@ListItem{'          ,
    'listItemClose'        : '}'                   ,
    'numlistOpen'          : '@NumberedList'       ,
    'numlistClose'         : '@EndList'            ,
    'numlistItemOpen'      : '@ListItem{'          ,
    'numlistItemClose'     : '}'                   ,
    'deflistOpen'          : '@TaggedList'         ,
    'deflistClose'         : '@EndList'            ,
    'deflistItem1Open'     : '@DropTagItem {'      ,
    'deflistItem1Close'    : '}'                   ,
    'deflistItem2Open'     : '{'                   ,
    'deflistItem2Close'    : '}'                   ,
    'bar1'                 : '@DP @FullWidthRule'  ,
    'url'                  : '{blue @Colour { \a }}'      ,
    'urlMark'              : '\a ({blue @Colour { \a }})' ,
    'email'                : '{blue @Colour { \a }}'      ,
    'emailMark'            : '\a ({blue Colour{ \a }})'   ,
    'img'                  : '~A~@IncludeGraphic { \a }'  ,  # eps only!
    '_imgAlignLeft'        : '@LeftDisplay '              ,
    '_imgAlignRight'       : '@RightDisplay '             ,
    '_imgAlignCenter'      : '@CentredDisplay '           ,
    # lout tables are *way* complicated, no support for now
    #'tableOpen'            : '~A~@Tbl~B~\naformat{ @Cell A | @Cell B } {',
    #'tableClose'           : '}'     ,
    #'tableRowOpen'         : '@Rowa\n'       ,
    #'tableTitleRowOpen'    : '@HeaderRowa'       ,
    #'tableCenterAlign'     : '@CentredDisplay '         ,
    #'tableCellOpen'        : '\a {'                     ,  # A, B, ...
    #'tableCellClose'       : '}'                        ,
    #'_tableBorder'         : '\nrule {yes}'             ,
    'comment'              : '# \a'                     ,
    # @MakeContents must be on the config file
    'TOC'                  : '@DP @ContentsGoesHere @DP',
    'pageBreak'            : '@NP'                      ,
    'EOD'                  : '@End @Text'
}

RULES = {
    'keepquoteindent': 1,
    'deflisttextstrip': 1,
    'escapeurl': 1,
    'verbblocknotescaped': 1,
    'imgalignable': 1,
    'mapbar2pagebreak': 1,
    'titleblocks': 1,
    'autonumberlist': 1,
    'parainsidelist': 1,

    'blanksaroundpara': 1,
    'blanksaroundverb': 1,
    # 'blanksaroundquote': 1,
    'blanksaroundlist': 1,
    'blanksaroundnumlist': 1,
    'blanksarounddeflist': 1,
    'blanksaroundtable': 1,
    'blanksaroundbar': 1,
    'blanksaroundtitle': 1,
    'blanksaroundnumtitle': 1,
}