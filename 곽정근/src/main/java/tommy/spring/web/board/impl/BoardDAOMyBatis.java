package tommy.spring.web.board.impl;

import java.util.List;

import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import tommy.spring.web.board.BoardVO;

@Repository
public class BoardDAOMyBatis {
	@Autowired
	private SqlSessionTemplate sqlSessionTemplate;

	public void insertBoard(BoardVO vo) {
		System.out.println("---> MyBatis로 insertBoard() 기능 처리");
		sqlSessionTemplate.insert("BoardDAO.insertBoard", vo);
	}

	public void updateBoard(BoardVO vo) {
		System.out.println("---> MyBatis로 updateBoard() 기능 처리");
		sqlSessionTemplate.update("BoardDAO.updateBoard", vo);
	}

	public void deleteBoard(BoardVO vo) {
		System.out.println("---> MyBatis로 deleteBoard() 기능 처리");
		sqlSessionTemplate.delete("BoardDAO.deleteBoard", vo);
	}

	public BoardVO getBoard(BoardVO vo) {
		System.out.println("---> MyBatis로 getBoard() 기능 처리");
		return (BoardVO) sqlSessionTemplate.selectOne("BoardDAO.getBoard", vo);
	}

	public List<BoardVO> getBoardList(BoardVO vo) {
		System.out.println("---> MyBatis로 getBoardList() 기능 처리");
		return sqlSessionTemplate.selectList("BoardDAO.getBoardList", vo);
	}
}
